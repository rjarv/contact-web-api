-- Table: address.family_key

-- DROP TABLE address.family_key;

CREATE TABLE address.family_key
(
  lastname character varying(30) NOT NULL, -- Paternal Surname/Maiden Name
  uid serial NOT NULL,
  CONSTRAINT family_key_pkey PRIMARY KEY (uid)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE address.family_key
  OWNER TO admin;
GRANT ALL ON TABLE address.family_key TO admin;
GRANT ALL ON TABLE address.family_key TO public;
GRANT ALL ON TABLE address.family_key TO app_user;
COMMENT ON COLUMN address.family_key.lastname IS 'Paternal Surname/Maiden Name';


