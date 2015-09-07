-- Domain: zipcode

-- DROP DOMAIN zipcode;

CREATE DOMAIN zipcode
  AS character varying(10)
  COLLATE pg_catalog."default"
  CONSTRAINT valid_zipcode CHECK (VALUE::text ~ '(^\d{5}(-\d{4})?$)|(^[ABCEGHJKLMNPRSTVXY]{1}\d{1}[A-Z]{1} *\d{1}[A-Z]{1}\d{1}$)'::text);
ALTER DOMAIN zipcode
  OWNER TO postgres;