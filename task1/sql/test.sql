CREATE OR REPLACE FUNCTION counter()
RETURNS TABLE (sum_ numeric, avg_ double precision) as
$$
 SELECT SUM(int_numbers), AVG(float_numbers) FROM public."Table1";
$$
LANGUAGE SQL;



select * from public.counter() p;
