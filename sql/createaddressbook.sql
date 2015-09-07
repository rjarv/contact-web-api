-- Table: address.address_book

-- DROP TABLE address.address_book;

CREATE TABLE address.address_book
(
  uid serial NOT NULL,
  first_name character varying(30),
  middle_name character varying(30),
  last_name character varying(30),
  address1 character varying(75),
  address2 character varying(50),
  city character varying(50),
  st_prvnce character varying(75),
  country character varying(75),
  zip zipcode,
  fam_key integer, -- References the address.family_key table.
  spouse_key integer, -- References the address.spousal_lineage_key table.
  CONSTRAINT address_book_fam_key_fkey FOREIGN KEY (fam_key)
      REFERENCES address.family_key (uid) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT address_book_spouse_key_fkey FOREIGN KEY (spouse_key)
      REFERENCES address.spousal_lineage_key (uid) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE address.address_book
  OWNER TO admin;
GRANT ALL ON TABLE address.address_book TO admin;
GRANT ALL ON TABLE address.address_book TO public;
COMMENT ON COLUMN address.address_book.fam_key IS 'References the address.family_key table.';
COMMENT ON COLUMN address.address_book.spouse_key IS 'References the address.spousal_lineage_key table.';