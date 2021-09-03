SELECT 
    MONTHNAME(charged_datetime) AS 'month',
    SUM(amount) AS revenue
	FROM billing
	WHERE charged_datetime >= '2012/03/01' AND charged_datetime < '2012/04/01';

SELECT 
    client_id,
    SUM(amount) AS total_revenue
	FROM billing
	WHERE client_id=2;
       
SELECT
	domain_name AS website,
    client_id 
	FROM sites
	WHERE client_id = 10;   

SELECT
	clients.client_id, COUNT(sites.domain_name) AS number_of_websites, MONTHNAME(sites.created_datetime) AS month_created, YEAR(sites.created_datetime) AS year_created
    FROM clients
    JOIN sites ON clients.client_id = sites.client_id AND clients.client_id = 1
GROUP BY MONTH(sites.created_datetime), YEAR(sites.created_datetime)
ORDER BY YEAR(sites.created_datetime);

SELECT
	clients.client_id, COUNT(sites.domain_name) AS number_of_websites, MONTHNAME(sites.created_datetime) AS month_created, YEAR(sites.created_datetime) AS year_created
    FROM clients
    JOIN sites ON clients.client_id = sites.client_id AND clients.client_id = 20
GROUP BY MONTH(sites.created_datetime), YEAR(sites.created_datetime)
ORDER BY YEAR(sites.created_datetime);

SELECT
	sites.domain_name AS website, COUNT(leads.leads_id) AS number_of_leads, DATE_FORMAT(leads.registered_datetime, '%M %d, %Y') AS date_generated
    FROM sites
    JOIN leads ON sites.site_id = leads.site_id
        AND leads.registered_datetime >= '2011-01-01'
        AND leads.registered_datetime <= '2011-02-15'
GROUP BY sites.domain_name;

SELECT
	CONCAT(clients.first_name,' ', clients.last_name) AS client_name, COUNT(leads.leads_id) AS number_of_leads
    FROM clients
    LEFT JOIN sites ON clients.client_id = sites.client_id
	LEFT JOIN leads ON sites.site_id = leads.site_id
    WHERE leads.leads_id >0
        AND leads.registered_datetime >= '2011-01-01'
        AND leads.registered_datetime <= '2011-12-31'
GROUP BY clients.client_id
ORDER BY clients.client_id;

SELECT
	CONCAT(clients.first_name,' ', clients.last_name) AS client_name, COUNT(leads.leads_id) AS number_of_leads, MONTHNAME(leads.registered_datetime) AS month_generated
    FROM clients
    LEFT JOIN sites ON clients.client_id = sites.client_id
	JOIN leads ON sites.site_id = leads.site_id
    WHERE leads.leads_id >0
        AND leads.registered_datetime >= '2011-01-01'
        AND leads.registered_datetime < '2011-07-01'
GROUP BY clients.client_id, MONTH(leads.registered_datetime)
ORDER BY MONTH(leads.registered_datetime);
    
SELECT
CONCAT(clients.first_name,' ',clients.last_name) AS client_name, sites.domain_name AS website, COUNT(leads.leads_id) AS number_of_leads, DATE_FORMAT(leads.registered_datetime, '%M %d, %Y') AS date_generated
FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
JOIN leads ON sites.site_id = leads.site_id
        AND leads.registered_datetime >= '2011-01-01'
        AND leads.registered_datetime <= '2011-12-31'
GROUP BY sites.domain_name
ORDER BY clients.client_id, sites.site_id;

SELECT
CONCAT(clients.first_name,' ',clients.last_name) AS client_name, sites.domain_name AS website, COUNT(leads.leads_id) AS number_of_leads
FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
JOIN leads ON sites.site_id = leads.site_id
GROUP BY sites.domain_name
ORDER BY clients.client_id, sites.site_id;

SELECT
CONCAT(clients.first_name,' ',clients.last_name) AS client_name, SUM(billing.amount) AS Total_Revenue, MONTHNAME(billing.charged_datetime) AS month_charge, YEAR(billing.charged_datetime) AS year_charge
FROM clients
JOIN billing ON clients.client_id = billing.client_id
GROUP BY clients.client_id , MONTH(billing.charged_datetime)
ORDER BY clients.client_id, YEAR(billing.charged_datetime), MONTH(billing.charged_datetime);

SELECT
	CONCAT(clients.first_name,' ',clients.last_name) AS client_name, GROUP_CONCAT(DISTINCT sites.domain_name SEPARATOR ' / ') AS sites
    FROM clients
    LEFT JOIN sites ON clients.client_id = sites.client_id
    GROUP BY clients.client_id
	ORDER BY clients.client_id, sites.site_id;
   
