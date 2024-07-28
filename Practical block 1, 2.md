ssh 57a18e5d-01e3-445c-b282-7a7989f6f867@serverhub.praktikum-services.ru -p 4554

psql -U morty -d scooter_rent

smith


select "Couriers"."login", count("inDelivery") 
from "Orders" 
inner join "Couriers" on "Couriers"."id" = "Orders"."courierId" 
where "inDelivery" = true 
group by "Couriers"."login";



select 
"track",
case 
when "finished" = true then 2
when "cancelled" = true then -1
when "inDelivery" = true then 1 
else 0
end as status
from "Orders";