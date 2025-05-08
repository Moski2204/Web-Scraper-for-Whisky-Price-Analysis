-- creating a new staging table
CREATE TABLE whiskey_data_staging
LIKE whiskey_data;

-- staging table has been created but has no data
SELECT *
FROM whiskey_data_staging;

-- insert data into the staging table
INSERT whiskey_data_staging
SELECT *
FROM whiskey_data;

-- Now data shows 
SELECT *
FROM whiskey_data_staging;

-- Rename column name
ALTER TABLE whiskey_data_staging
RENAME COLUMN name to Name;

ALTER TABLE whiskey_data_staging
RENAME COLUMN price to Price;

ALTER TABLE whiskey_data_staging
RENAME COLUMN litre to Litre;

-- removing the Â from the data
UPDATE whiskey_data_staging
SET Price = REPLACE(Price, 'Â', ''), Litre = REPLACE(Litre, 'Â', '');

SELECT *
FROM whiskey_data_staging;

-- remove the 'per litre' in Litre
UPDATE whiskey_data_staging
SET Litre = REPLACE(Litre, 'per litre', '/L');

-- remove the pounds symbol in price.
UPDATE whiskey_data_staging
SET Price = REPLACE(Price, '£', '');

ALTER TABLE whiskey_data_staging
RENAME COLUMN `Price` TO `PriceInPounds`;

ALTER TABLE whiskey_data_staging
RENAME COLUMN  `Price(£)` TO `Price (£)`;

SELECT *
FROM whiskey_data_staging;

-- lowest to highest
	-- did it like this because it wasn't doing it properly before
	-- MySQL will coerce a numeric context if you add zero. This works too:
	-- Because your Price (£) column is still text, MySQL is sorting it lexically (“139” before “50.50” because “1” < “5”) 
	-- and you’re also using ASC (lowest→highest).
	-- To get the true highest prices at the top, do two things: convert it to a number Sort descending
SELECT *
FROM whiskey_data_staging
ORDER BY (`Price (£)` + 0) ASC;

-- highest to lowest 
SELECT *
FROM whiskey_data_staging
ORDER BY (`Price (£)` + 0) DESC;


