create table events(id int, event_name varchar(40), people_count int);
insert into  events values (1,'event_1', 25);

insert into  events values(2,'event_2', 250);

insert into  events values(3,'event_3', 300);

insert into  events values(4,'event_4', 450);

insert into  events values(5,'event_5', 50);

insert into  events values(6,'event_6', 75);

insert into  events values(7,'event_7', 101);

insert into  events values(8,'event_8', 150);

insert into  events values(9,'event_9', 160);
insert into  events values(10,'event_10', 25);
insert into  events values(11,'event_11', 200);
insert into  events values(12,'event_12', 225);
insert into  events values(13,'event_13', 25);
insert into  events values(14,'event_14', 25);


WITH events_cte
AS
(
	SELECT sub.id,sub.event_name,sub.people_count,COUNT(1) OVER(PARTITION BY num_cnt) total_cnt  FROM
	(
		SELECT e.id ,e.event_name,e.people_count
		   ,(SELECT COUNT(id) FROM events WHERE people_count <= 100 AND ID < e.id) AS num_cnt
		FROM  events e
		WHERE people_count > 100
	) sub
)

SELECT id, event_name, people_count FROM events_cte WHERE total_cnt >= 3;