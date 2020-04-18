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
		      r_price float,r_availability BOOLEAN )
create table payment(payment_id serial primary key,payment_type varchar(100),payment_total float,
		     o_id integer references resource_order(o_id));
create table resource_order(o_id serial primary key, o_date DATE NULL DEFAULT CURRENT_DATE,o_quantity integer,r_list TEXT, order_total_price float);

/* Relations*/
create table supplies(supplier_id integer references supplier(s_id),
		      r_id integer references resource(r_id),supply_date DATE NULL DEFAULT CURRENT_DATE, primary key(supplier_id,r_id));
create table reserves(p_id integer references person(p_id),r_id integer references resource(r_id), reserve_date DATE NULL DEFAULT CURRENT_DATE,
		      , resource_total integer, primary key(p_id,r_id));
create table requests(p_id integer references person(p_id),r_id integer references resource(r_id)
		      ,request_date DATE NULL DEFAULT CURRENT_DATE, request_quantity integer, primary key(p_id,r_id));
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

/*Senate Region Computation Function*/
create function get_senate_region(r_location varchar(150)) returns varchar(150) as $$
begin
	if r_location='Aguas Buenas' or  r_location='Guaynabo' or r_location='San Juan' then return 'San Juan';
	elsif r_location='Bayamon' or r_location='Cataño' or r_location='Toa Alta' or r_location='Toa Baja' then return 'Bayamon';
	elsif r_location='Arecibo' or r_location='Barceloneta' or r_location='Camuy' or r_location='Ciales' or r_location='Dorado' or r_location='Florida' or r_location='Hatillo' or r_location='Manati' or r_location='Morovis' or r_location='Quebradillas' or r_location='Vega Alta' or r_location='Vega Baja' then return 'Arecibo';
   	elsif r_location='Aguada' or r_location='Aguadilla' or r_location='Añasco' or r_location='Cabo Rojo' or r_location='Hormigueros' or r_location='Isabela' or r_location='Las Marias' or r_location='Mayaguez' or r_location='Moca' or r_location='Rincon' or r_location='San German' or r_location='San Sebastian' then return 'Mayaguez-Aguadilla';
   	elsif r_location='Adjuntas' or r_location='Guanica' or r_location='Guayanilla' or r_location='Jayuya' or r_location='Juana Diaz' or r_location='Lajas' or r_location='Lares' or r_location='Maricao' or r_location='Peñuelas' or r_location='Ponce' or r_location='Sabana Grande' or r_location='Utuado' or r_location='Yauco' then return 'Ponce';
   	elsif r_location='Aibonito' or r_location='Arroyo' or r_location='Barranquitas' or r_location='Cayey' or r_location='Cidra' or r_location='Coamo' or r_location='Comerio' or r_location='Corozal' or r_location='Guayama' or r_location='Naranjito' or r_location='Orocovis' or r_location='Salinas' or r_location='Santa Isabel' or r_location='Villalba' then return 'Guayama';
	elsif r_location='Caguas' or r_location='Gurabo' or r_location='Humacao' or r_location='Juncos' or r_location='Las Piedras' or r_location='Maunabo' or r_location='Naguabo' or r_location='Patillas' or r_location='San Lorenzo' or r_location='Yabucoa' then return 'Humacao';
	elsif r_location='Canovanas' or r_location='Carolina' or r_location='Ceiba' or r_location='Culebra' or r_location='Fajardo' or r_location='Loiza' or r_location='Luquillo' or r_location='Rio Grande' or r_location='Trujillo Alto' or r_location='Vieques' then return 'Carolina';
	end if;
end $$
language plpgsql;