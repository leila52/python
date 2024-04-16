/*control join +funciones
Muestra el nombre y apellidos de los empleados que fueron contratados el mismo día de la semana que ingresaron en un departamento (pero sin ser la misma fecha) así como el día del mes que dejaron su departamento coincida con el día del mes de su fecha de nacimiento. Además, su apellido debe contener "cz".
Resultado:
*/
select first_name, last_name
from
    employees e
    join dept_emp de
    join departments d on e.emp_no = de.emp_no
    and d.dept_no = de.dept_no
where
    date_format(de.from_date, "%W") = date_format(e.hire_date, "%W")
    and de.from_date != e.hire_date
    and day(de.to_date) = day(e.birth_date)
    and last_name like "%cz%";

Muestra el nombre de los empleados que fueron mánagers y sus salarios de más de 10 años después de dejar de ser mánagers. De los salarios mostrar la fecha en el formato numérico del resultado, y el salario en los miles completos que tiene. Entre paréntesis de indica el año en que dejó de ser mánager.
Resultado:
select concat(e.first_name, " (",year(dm.to_date),")") as emp, date_format(s.from_date,"%d de %m de %y") as fecha_salario, truncate(s.salary/1000,0) as miles from dept_manager dm join employees e join salaries s on s.emp_no = e.emp_no and e.emp_no = dm.emp_no where timestampdiff(year,dm.to_date,s.from_date) > 10;

Muestra el departamento, el nombre y apellidos juntos y los años que han estado en el departamento, siempre que tardasen entre 16 y 17 años en obtener un titulo que no sea "Senior". (Coincide la antigüedad y los años que tardan, pero no hay relación)


select
    dept_name,
    concat(
        e.first_name, " ", e.last_name
    ) as empleado,
    timestampdiff(
        year, de.from_date, de.to_date
    ) as antiguedad
from
    titles t
    join employees e
    join dept_emp de
    join departments d on t.emp_no = e.emp_no
    and e.emp_no = de.emp_no
    and de.dept_no = d.dept_no
where
    timestampdiff(year, t.from_date, t.to_date) between 16 and 17
    and title not like "Senior%";

Muestra el nombre y apellidos, sus títulos y el tiempo que los que fueron mánagers (ya no lo son), pero lo fueron durante más de 5 años.


select concat(
        left(first_name, 1), ". ", last_name
    ) as manager, title, timestampdiff(
        year, dm.from_date, dm.to_date
    ) as "años"
from
    dept_manager dm
    join employees e
    join titles t on dm.emp_no = e.emp_no
    and e.emp_no = t.emp_no
    and timestampdiff(
        year, dm.from_date, dm.to_date
    ) > 5
    and year(dm.to_date) < 9999;

join group GROUP BY

Muestra cuántos empeados hay por inicial y año de finalización de su titulación,
mostrando también su salario más alto,
siempre que el número de empleados sea menor que 3.
select
    left(first_name, 1) as inicial,
    year(t.to_date) as finaliza,
    count(*) as num,
    max(s.salary) as salario
from
    employees e
    join titles t
    join salaries s on e.emp_no = t.emp_no
    and e.emp_no = s.emp_no
group by
    inicial,
    finaliza
having
    num < 3
order by num;

 Selecciona para cada departamento los años de antigüedad en el departamento del empleado que más llevaba en el departamento el 1 de enero de 2004 y los años del que menos. Los empleados deben seguir en el departamento actualmente.
Resultado:
select dept_name, max(timestampdiff(year,de.from_date,"2004-01-01")) mas_ant, min(timestampdiff(year,de.from_date,"2004-01-01")) as menos_ant from departments d join dept_emp de on d.dept_no = de.dept_no where year(to_date) = 9999 group by dept_name;

Selecciona el número de empleados que terminó una titulación y cuántos años tardaron en hacerlo, siempre que sean mujeres y su salario sea superior a 100000. Mostrar solo los años (de duración) en los que menos de 1000 empleados acabaron su titulación, y ordenarlo por años.
Resultado:
/*timestampdiff te muestra la diferencia de dias*/
select timestampdiff(year,t.from_date,t.to_date) as anios, count(*) as num from titles t join employees e join salaries s on e.emp_no = t.emp_no and e.emp_no = s.emp_no where year(t.to_date) < 9999 and e.gender = "F" and s.salary > 100000 group by anios having num < 1000 order by anios;

Muestra por departamento la media de salarios actuales,
y el número de ellos de los empleados contratados después de 1990,
mostrando solo los departamentos cuya media se inferior a 70000.

select dept_name, avg(salary) as media, count(salary) as num
from
    departments d
    join dept_emp de
    join employees e
    join salaries s on d.dept_no = de.dept_no
    and de.emp_no = e.emp_no
    and e.emp_no = s.emp_no
where
    year(hire_date) > 1990
    and year(s.to_date) = 9999
group by
    dept_name
having
    media < 70000;

/*dificil */
Selecciona la inicial y el apellido de los empleados, su primer salario y el año (comienzo) de ese salario, su último salario y el año (comienzo) de ese salario, así como cuántos años han pasado entre esos salarios y el número total de salarios que ha tenido, de aquellos que nacieron el mismo día de la semana que el día de la semana que fueron contratados, y además que desde el primer salario hasta el último este se ha incrementado en más de 2.25 (de 10000 pasaría a 22501 o más). También han de haber pasado más de 15 años entre el primer y último salario.


select
    concat(
        left(first_name, 1), ". ", last_name
    ) as emp,
    min(salary) as prim_sal,
    min(year(from_date)) as primer,
    max(salary) as ult_sal,
    max(year(from_date)) as ultimo,
    timestampdiff(
        year, min(from_date), max(from_date)
    ) as "años",
    count(*) as num
from salaries s
    join employees e on s.emp_no = e.emp_no
group by
    s.emp_no
having
    años > 15
    and min(salary) * 2.25 < max(salary);

Muestra por cada década de contrato y cada década de comienzo de estudio de título,
cuantos títulos de cualquier tipo de ingeniería fueron conseguidos por sus empleados.Motrar solo las décadas en las que sean más de 1000 títulos.Tener dos columnas de décadas significa,
por ejemplo que un 80 -80 es cuántos títulos de empleados contratados en los 80 y títulos finalizados en los 80. Mientras que un 80 -90 sería empleados contratados en los 80 con títulos de los 90.

select (
        truncate (year(hire_date) / 10, 0) % 10
    ) * 10 as decada_contrato,
    (
        truncate (year(t.from_date) / 10, 0) % 10
    ) * 10 as decada_titulo,
    count(*) as num
from titles t
    join employees e on t.emp_no = e.emp_no
where
    title like "%Engi%"
group by
    decada_contrato,
    decada_titulo
having
    num > 1000
order by decada_contrato;

Un trienio lo cumple un empleado cuando tiene 3 años completos de contrato. Muestra cuántos empleados tenían cuántos trienios el 1 de enero de 2002, así como la suma de sus salarios (en millones con dos decimales), de sus salarios actuales. Ordenarlo por el número de trienios.


select
truncate (
    timestampdiff(year, hire_date, "2002-01-01") / 3, 0
) as trienio,
count(*) as num,
round(sum(salary) / 1000000, 2) as millones
from employees e
    join salaries s on e.emp_no = s.emp_no
where
    year(s.to_date) = 9999
group by
    trienio
order by trienio;

Selecciona el nombre y apellidos juntos de cada mánager que ha habido en el departamento "Customer Service" y el número de empleados que pasaron por su departamento mientras fueron mánagers (esto es entraron en el departamento a la vez o después que el mánager y salieron antes o a la vez), siempre que sean menos de 1000 empleados.


select concat(e.first_name, e.last_name) as manager, count(distinct de.emp_no) as num
from
    employees e
    join dept_emp de
    join dept_manager dm
    join departments d on e.emp_no = dm.emp_no
    and dm.dept_no = d.dept_no
    and de.dept_no = d.dept_no
    and de.from_date >= dm.from_date
    and de.to_date <= dm.to_date
where
    dept_name = "Customer Service"
group by
    manager
having
    num < 1000;

/*autojoin dificil*/
Selecciona mánagers que estén en el cargo junto a empleadas de su departamento que llevaban 3 veces más días que su mánager el 1 de enero de 2002 y tienen más edad. Además, las empleadas no deben tener un título que tengan 100000 o más empleados o empleadas.
Los nombres de mánagers y empleadas han de mosrtarse solo los dos primeros caracteres del nombre y los dos últimos del apellido separados por espacio. De las empleadas además el número de empleada.
Resultado:
select concat(left(e1.first_name,2)," ",right(e1.last_name,2)) as jefe, concat(left(e2.first_name,2)," ",right(e2.last_name,2)) as empleada, e2.emp_no from employees e1 join employees e2 join dept_manager d join dept_emp de on e1.emp_no = d.emp_no and e2.emp_no = de.emp_no and d.dept_no = de.dept_no where e2.emp_no not in (select emp_no from titles where title not in (select title from titles group by title having count(*) > 100000)) and e1.birth_date < e2.birth_date and year(d.to_date) = 9999 and timestampdiff(day,de.from_date,"2002-01-01") > (timestampdiff(day,d.from_date,"2002-01-01"))*3 and e2.gender = "F";

Un trienio lo cumple un empleado cuando tiene 3 años completos de contrato. Muestra cuántos empleados tenían cuántos trienios el 1 de enero de 2002, así como la suma de sus salarios (en millones con dos decimales), de sus salarios actuales, así como el coste de incrementar los salarios un 2% por cada trienio.
Muestra en una última linea el número total de empleados, los millones que cuestan los salarios y el coste total del incremento salarial por trienios.
Ordenarlo por el número de trienios y al final el total
Resultado:
select trienio, num, millones, trienio*millones*0.02 as coste from (select truncate(timestampdiff(year,hire_date,"2002-01-01")/3,0) as trienio, count(*) as num, sum(salary)/1000000 as millones from employees e join salaries s on e.emp_no = s.emp_no where year(s.to_date) = 9999 group by trienio order by trienio) s1 union select "total", sum(num),sum(millones), sum(millones*trienio*0.02) from (select truncate(timestampdiff(year,hire_date,"2002-01-01")/3,0) as trienio, count(*) as num, sum(salary)/1000000 as millones from employees e join salaries s on e.emp_no = s.emp_no where year(s.to_date) = 9999 group by trienio order by trienio) as s2;

Mostrar la mitad del nombre del empleado y del apellido, separados por un punto, y el incremento salarial en porcentaje con dos decimales ( y el símbolo %) que tuvo el mismo día que finalizó su titulación, mostrando también la titulación, pero solo de aquellos empleados que fueron contratados el mismo mes del mismo año que comenzó el mánager de su departamento con ese cargo.
Resultado:
select concat(left(e.first_name,length(first_name)/2),".",left(e.last_name,length(last_name)/2))as emp, concat(round((s2.salary/s1.salary)*100-100,2),"%") as incremento,t.title,t.to_date  
from
    employees e
    join titles t
    join salaries s1
    join salaries s2 on e.emp_no = s1.emp_no
    and e.emp_no = t.emp_no
    and e.emp_no = s2.emp_no
    and t.to_date = s2.from_date
    and s1.to_date = s2.from_date
where e.emp_no in(
    select de.emp_no
    from
        dept_emp de
        join employees e2
        join dept_manager dm on dm.dept_no = de.dept_no
        and e2.emp_no = de.emp_no
        and month(e2.hire_date) = month(dm.from_date)
        and year(e2.hire_date) = year(dm.from_date)
)
order by incremento;

/*cuestionario 4*/
Muestra el código de empleado y los títulos que tiene cada mánager que siga siendo mánager y pasase menos de 5 años desde que fue contratado a tener cargo de mánager.
El código es la inicial del nombre, punto y las tres primeras letras del apellido.
Resultado:
select concat(left(first_name,1),".",left(last_name,3)) as cod_emp, title from dept_manager dm join employees e join titles t on dm.emp_no = e.emp_no and e.emp_no = t.emp_no where year(dm.to_date) = 9999 and timestampdiff(year,e.hire_date,dm.from_date) < 5;

Muestra el departamento y su extensión mánager así como su salario actual si es superior a 100000.
La extensión son los tres primeros caracteres del nombre y los tres últimos del apellido separados por punto.
Resultado:
select dept_name, concat(left(first_name,3),".", right(last_name,3)) as ext_empleado, salary from departments d join dept_manager dm join employees e join salaries s on d.dept_no = dm.dept_no and dm.emp_no = e.emp_no and e.emp_no = s.emp_no where salary > 100000 and year(s.to_date) = 9999;

Muestra el nombre y apellidos de los empleados y su salario de aquellos cuyo salario supera los 90000 y  comenzaron en un departamento el mismo año que comienza su salario, siendo posterior a 2000. También ha de coincidir que el día del mes que comenzaron en el departamento sea el 31 de cualquier mes.
Resultado:
select concat(first_name," ",last_name) as emp, salary from dept_emp de join employees e join salaries s on de.emp_no = e.emp_no and e.emp_no = s.emp_no where year(s.from_date) = year(de.from_date) and year(de.from_date) > 2000 and day(de.from_date) = 31 and salary > 90000;

Muestra el nombre y apellidos, el título que posea siempre que sea "Senior" y el salario que tenía cuando fue contratado. De estos, mostrar solo los 10 salarios más altos.
Resultado:
select concat(first_name, " ", last_name) as emp, title, salary from titles t join employees e join salaries s on t.emp_no = e.emp_no and e.emp_no = s.emp_no where hire_date = s.from_date and title like "%Senior%" order by salary desc limit 10;

/*cuestionario 9*/

Muestra cuántos empeados hay por inicial y año de finalización de su titulación, mostrando también su salario más alto, siempre que el número de empleados sea menor que 3.
Resultado:
select left(first_name,1) as inicial, year(t.to_date) as finaliza, count(*) as num, max(s.salary) as salario from employees e join titles t join salaries s on e.emp_no = t.emp_no and e.emp_no = s.emp_no group by inicial, finaliza having num < 3 order by num;

Selecciona para cada departamento los años de antigüedad en el departamento del empleado que más llevaba en el departamento el 1 de enero de 2004 y los años del que menos. Los empleados deben seguir en el departamento actualmente.
Resultado:
select dept_name, max(timestampdiff(year,de.from_date,"2004-01-01")) mas_ant, min(timestampdiff(year,de.from_date,"2004-01-01")) as menos_ant from departments d join dept_emp de on d.dept_no = de.dept_no where year(to_date) = 9999 group by dept_name;

Selecciona el número de empleados que terminó una titulación y cuántos años tardaron en hacerlo, siempre que sean mujeres y su salario sea superior a 100000. Mostrar solo los años en los que menos de 1000 empleados acabaron su titulación, y ordenarlo por años.
Resultado:
select timestampdiff(year,t.from_date,t.to_date) as anios, count(*) as num from titles t join employees e join salaries s on e.emp_no = t.emp_no and e.emp_no = s.emp_no where year(t.to_date) < 9999 and e.gender = "F" and s.salary > 100000 group by anios having num < 1000 order by anios;

Muestra por departamento la media de salarios actuales, y el número de ellos de los empleados contratados después de 1990, mostrando solo los departamentos cuya media se inferior a 70000.
Resultado:
select dept_name, avg(salary) as media, count(salary) as num from departments d join dept_emp de join employees e join salaries s on d.dept_no = de.dept_no and de.emp_no = e.emp_no and e.emp_no = s.emp_no where year(hire_date)> 1990 and year(s.to_date) = 9999 group by dept_name having media < 70000;

Selecciona el apellido del empleado más novato del departamento del jefe de departamento más joven de los jefes de departamento más veteranos.Muestra el apellido del empleado con el apellido del jefe entre paréntesis,
y las fechas de incorporación de ambos,
as í como el nombre del departamento.select concat(
    e2.last_name, " (", e.last_name, ")"
),
e2.hire_date,
d.dept_name,
d.dept_name,
de.dept_no
from
    employees e
    join dept_manager m
    join departments d
    join employees e2
    join dept_emp de on e.emp_no = m.emp_no
    and m.dept_no = d.dept_no
    and e2.emp_no != e.emp_no
    and e2.emp_no = de.emp_no
    and de.dept_no = m.dept_no
where
    e.birth_date = (
        select max(birth_date)
        from employees
        where
            hire_date = (
                select min(hire_date)
                from employees
            )
    )
    and e.hire_date = (
        select min(hire_date)
        from employees
    )
    and e2.hire_date = (
        select max(hire_date)
        from employees e3
            join dept_emp d3 on e3.emp_no = d3.emp_no
        where
            dept_no = (
                select dept_no
                from employees e3
                    join dept_manager d3 on e3.emp_no = d3.emp_no
                where
                    e3.birth_date = (
                        select max(birth_date)
                        from employees
                        where
                            hire_date = (
                                select min(hire_date)
                                from employees
                            )
                    )
            )
    );