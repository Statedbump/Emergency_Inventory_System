create table login(login_id serial primary key, username varchar(100), password varchar(100));

/* Specialization of Login*/											
create table person(p_id serial primary key,first_name varchar(100),
		    middle_initial varchar(3),last_name varchar(100),email varchar(320),
		    location_of_p varchar(300),phone varchar(15),login_id integer references login(login_id));
create table supplier(s_id serial primary key, first_name varchar(100),middle_initial char(3),
		      last_name varchar(100), company_name varchar(150),warehouse_address varchar(200),
		      supplier_location varchar(300),phone varchar(15),login_id integer references login(login_id));

/* Specialization of Person*/													 
create table administrator(admin_id serial primary key, permission_key varchar(100),p_id integer references person(p_id));

create table resource(r_id serial primary key,r_type varchar(100),r_quantity integer,r_location varchar(150),
		      r_price float,r_availability BOOLEAN );
create table payment(payment_id serial primary key,payment_type varchar(100),payment_total float,
		     o_id integer references resource_order(o_id));
create table resource_order(o_id serial primary key,o_date DATE,o_quantity integer,r_list TEXT, order_total_price float);

/* Relations*/
create table supplies(supplier_id integer references supplier(supplier_id),
		      r_id integer references resource(r_id),supplyin_date DATE , primary key(supplier_id,r_id));
create table requests(p_id integer references person(p_id),r_id integer references resource(r_id) 
		      ,request_date DATE, resource_total integer, primary key(p_id,r_id));
create table manages(admin_id integer references administrator(admin_id), r_id integer references resource(r_id));
create table buys(r_id integer references resource(r_id), o_id integer references resource_order(o_id),total_price float, resource_total integer,
		 primary key(r_id,o_id));
create table offers(p_id integer references person(p_id), payment_id integer references payment(payment_id),
		    primary key(p_id,payment_id));	     

/* Specialization of Resource*/
create table water(w_id serial primary key, water_type varchar(50),measurement_unit varchar(50),
		   r_id integer references resource(r_id));
create table fuel(fuel_id serial primary key,fuel_type varchar(50), fuel_octane_rating integer,
		  r_id integer references  resource(r_id));
create table food(food_id serial primary key,food_type varchar(100),r_id integer references resource(r_id));
