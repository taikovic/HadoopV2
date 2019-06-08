--query number 1: 
--ATL 

select t1.orig,t1.origin_count, t2.dest_count --,sum(t1.origin_count + t2.dest_count) as total 
from 
(select flights.origin_airport as orig, count(*) as origin_count from flights
group by flights.origin_airport
order by origin_count desc)t1
inner join 
(select flights.destination_airport as dest, count(*) as dest_count from flights
group by flights.destination_airport
order by dest_count desc)t2
on t1.orig=t2.dest


-- query number 2;
-- Hartsfield-Jackson Atlanta International Airport


select flights.origin_airport as orig,airports.airport as airportname, count(*) as origin_count from flights
inner join airports 
on airports.iata_code=flights.origin_airport
group by flights.origin_airport, airports.airport
order by origin_count desc
limit 1 

-- query number 3: 

select year, count(*) as nombre_flights from flights
group by flights.year
--5819079

--query number:4

select count(*) as cpt
from flights f
inner join airports oap
on f.origin_airport = oap.iata_code
inner join airports dap
on f.destination_airport = dap.iata_code
where oap.airport='Seattle-Tacoma International Airport'
or dap.airport='Seattle-Tacoma International Airport'

--query number: 5
--F2:4337
select flights.airline,count(*) as counts from flights
inner join airports 
on flights.destination_airport=airports.iata_code
where 1=1
and airports.city='Las Vegas'
group by flights.airline
order by 3 desc
limit 1

--query number: 6 
--Southwest Airlines Co. : 68516
select airlines.airline,count(*) as counts  from flights
inner join airports 
on flights.destination_airport=airports.iata_code
inner join airlines
on flights.airline=airlines.iata_code
where 1=1
and airports.city='Las Vegas'
group by flights.airline,airlines.airline
order by 4 desc
limit 1

