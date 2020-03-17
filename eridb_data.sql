insert into login(username, password) values ('Yetsiel123', 'ciic');
insert into supplier(first_name , middle_initial , last_name , company_name , warehouse_address ,supplier_location ,
                     phone ,login_id )
                    values ('Yetsiel','S','Aviles','Plaza Provision Company','PPC 123', 'San Juan','7871234567',1);
insert into resource(r_type ,r_quantity ,r_location ,r_price ,r_availability ) values('Batteries',6,'San Juan',5.00,True);
insert into person(first_name , middle_initial ,last_name ,email ,location_of_p ,phone ,login_id)
                    values ('Tito', 'M', 'Kayak','titokayak@gmail.com','Caguas','9399399999',2);
insert into resource(r_type,r_quantity,r_location,r_price,r_availability) values('Water',10,'San Juan',4.00,True);
insert into water(water_type,measurement_unit, r_id ) values('Small Bottles','ounces',2);
insert into resource(r_type ,r_quantity ,r_location ,r_price ,r_availability ) values('Fuel',1,'San Juan',20.0,True);
insert into fuel(fuel_type,fuel_octane_rating,r_id) values('Gasoline',87,3);
insert into resource(r_type ,r_quantity ,r_location ,r_price ,r_availability ) values('Food',16,'San Juan',0.00,True);
insert into food(food_type,r_id ) values('Baby Food',4);
insert into supplies(supplier_id , r_id ,supplyin_date ) values(1,1,'2020-04-17');
insert into supplies(supplier_id , r_id ,supplyin_date ) values(1,2,'2020-04-17');
insert into supplies(supplier_id , r_id ,supplyin_date ) values(1,3,'2020-04-17');
insert into supplies(supplier_id , r_id ,supplyin_date ) values(1,4,'2020-04-17');
insert into requests(p_id, r_id , request_date , resource_total) values (1,4,'2020-04-17',1);
insert into resource_order(o_date ,o_quantity ,r_list, order_total_price ) values('2020-04-17',3,
                    'Batteries, Gasoline Fuel, Nikini Water Bottles',29.00);
insert into payment (payment_type ,payment_total , o_id ) values('ATH Movil',29.00,1);
insert into offers(p_id ,payment_id ) values(1,1);
insert into buys(r_id,o_id ,total_price ,resource_total) values (1,1,5.00,1);
insert into buys(r_id,o_id ,total_price, resource_total ) values (2,1,4.00,1);
insert into buys(r_id,o_id ,total_price, resource_total ) values (3,1,20.00,1);







