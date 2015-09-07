-- Table: address.spousal_lineage_key

-- DROP TABLE address.spousal_lineage_key;

CREATE TABLE address.spousal_lineage_key
(
  lastname character varying(30) NOT NULL, -- Paternal Surname/Maiden Name
  uid serial NOT NULL,
  CONSTRAINT spousal_lineage_key_pkey PRIMARY KEY (uid)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE address.spousal_lineage_key
  OWNER TO admin;
GRANT ALL ON TABLE address.spousal_lineage_key TO admin;
GRANT ALL ON TABLE address.spousal_lineage_key TO public;
GRANT ALL ON TABLE address.spousal_lineage_key TO app_user;
COMMENT ON COLUMN address.spousal_lineage_key.lastname IS 'Paternal Surname/Maiden Name';