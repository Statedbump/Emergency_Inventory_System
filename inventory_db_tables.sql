create table login(login_id serial primary key, username varchar(100), password varchar(100));
create table person(p_id serial primary key,first_name varchar(100),
			middle_initial char(3),email varchar(320),
			location_of_p varchar(300), login_id integer references login(login_id));
create table supplier(supplier_id serial primary key, first_name varchar(100),
					  middle_initial char(3),last_name varchar(100), company_name varchar(150),
					  warehouse_address varchar(200),supplier_location varchar(300),
					  login_id integer references login(login_id)
					  );
create table administrator(admin_id serial primary key, p_id integer references person(p_id),permission_key varchar(100));

create table resource(r_id serial primary key,resource_type char(100)
,quantity integer,res_location varchar(150));

/* Relations*/
create table supplies(supplier_id integer references supplier(supplier_id),
r_id integer references resource(r_id),supplyin_date DATE , primary key(supplier_id,r_id));

create table requests(p_id integer references person(p_id),r_id integer references resource(r_id) 
,request_date DATE,primary key(p_id,r_id));

create table manages(admin_id integer references administrator(admin_id), r_id integer references resource(r_id));

/* Specialization */

create table water(w_id serial primary key,r_id integer references resource(r_id), water_type varchar(50),measurement_unit varchar(50),liquid_measurement integer );
create table Fuel(fuel_id serial primary key,r_id integer references  resource(r_id), fuel_type varchar(50), fuel_octane_rating integer );
create table Food(food_id serial primary key, r_id integer references resource(r_id),food_type varchar(100));
