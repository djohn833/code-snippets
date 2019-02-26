--
-- PostgreSQL database dump
--

-- Dumped from database version 10.0
-- Dumped by pg_dump version 10.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: postgres; Type: COMMENT; Schema: -; Owner: davejohnson
--

COMMENT ON DATABASE postgres IS 'default administrative connection database';


--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: operation; Type: TABLE; Schema: public; Owner: davejohnson
--

CREATE TABLE operation (
    id integer NOT NULL,
    name character varying(32) NOT NULL
);


ALTER TABLE operation OWNER TO davejohnson;

--
-- Name: operation_id_seq; Type: SEQUENCE; Schema: public; Owner: davejohnson
--

CREATE SEQUENCE operation_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE operation_id_seq OWNER TO davejohnson;

--
-- Name: operation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: davejohnson
--

ALTER SEQUENCE operation_id_seq OWNED BY operation.id;


--
-- Name: property; Type: TABLE; Schema: public; Owner: davejohnson
--

CREATE TABLE property (
    id integer NOT NULL,
    name character varying(32) NOT NULL,
    description character varying(256) NOT NULL
);


ALTER TABLE property OWNER TO davejohnson;

--
-- Name: property_id_seq; Type: SEQUENCE; Schema: public; Owner: davejohnson
--

CREATE SEQUENCE property_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE property_id_seq OWNER TO davejohnson;

--
-- Name: property_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: davejohnson
--

ALTER SEQUENCE property_id_seq OWNED BY property.id;


--
-- Name: structure; Type: TABLE; Schema: public; Owner: davejohnson
--

CREATE TABLE structure (
    id integer NOT NULL,
    name character varying(32) NOT NULL
);


ALTER TABLE structure OWNER TO davejohnson;

--
-- Name: structure_id_seq; Type: SEQUENCE; Schema: public; Owner: davejohnson
--

CREATE SEQUENCE structure_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE structure_id_seq OWNER TO davejohnson;

--
-- Name: structure_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: davejohnson
--

ALTER SEQUENCE structure_id_seq OWNED BY structure.id;


--
-- Name: structure_operation; Type: TABLE; Schema: public; Owner: davejohnson
--

CREATE TABLE structure_operation (
    structure_id integer NOT NULL,
    operation_id integer NOT NULL
);


ALTER TABLE structure_operation OWNER TO davejohnson;

--
-- Name: structure_operation_property; Type: TABLE; Schema: public; Owner: davejohnson
--

CREATE TABLE structure_operation_property (
    structure_id integer NOT NULL,
    operation_id integer NOT NULL,
    property_id integer NOT NULL
);


ALTER TABLE structure_operation_property OWNER TO davejohnson;

--
-- Name: operation id; Type: DEFAULT; Schema: public; Owner: davejohnson
--

ALTER TABLE ONLY operation ALTER COLUMN id SET DEFAULT nextval('operation_id_seq'::regclass);


--
-- Name: property id; Type: DEFAULT; Schema: public; Owner: davejohnson
--

ALTER TABLE ONLY property ALTER COLUMN id SET DEFAULT nextval('property_id_seq'::regclass);


--
-- Name: structure id; Type: DEFAULT; Schema: public; Owner: davejohnson
--

ALTER TABLE ONLY structure ALTER COLUMN id SET DEFAULT nextval('structure_id_seq'::regclass);


--
-- Data for Name: operation; Type: TABLE DATA; Schema: public; Owner: davejohnson
--

COPY operation (id, name) FROM stdin;
1	Binary operation
2	Addition
3	Multiplication
4	Composition of arrows
\.


--
-- Data for Name: property; Type: TABLE DATA; Schema: public; Owner: davejohnson
--

COPY property (id, name, description) FROM stdin;
1	Associativity	a*(b*c) = (a*b)*c
3	Invertibility	∀a ∃a⁻¹: a * a⁻¹ = a⁻¹ * a = e
4	Commutativity	a*b = b*a
2	Identity	∃e: a*e = e*a = a
5	Closure	∀a,b ∈ A: a*b ∈ A
\.


--
-- Data for Name: structure; Type: TABLE DATA; Schema: public; Owner: davejohnson
--

COPY structure (id, name) FROM stdin;
1	Group
2	Semigroup
3	Monoid
4	Quasigroup
5	Loop
6	Abelian Group
7	Magma
8	Inverse Semigroup
9	Semigroupoid
10	Category
11	Groupoid
12	Ring
13	Semiring
14	Commutative ring
15	Integral domain
16	Field
17	Division ring
\.


--
-- Data for Name: structure_operation; Type: TABLE DATA; Schema: public; Owner: davejohnson
--

COPY structure_operation (structure_id, operation_id) FROM stdin;
1	1
2	1
3	1
4	1
5	1
6	1
7	1
8	1
9	1
11	1
10	4
12	2
13	2
14	2
15	2
16	2
17	2
12	3
13	3
14	3
15	3
16	3
17	3
\.


--
-- Data for Name: structure_operation_property; Type: TABLE DATA; Schema: public; Owner: davejohnson
--

COPY structure_operation_property (structure_id, operation_id, property_id) FROM stdin;
1	1	1
1	1	2
1	1	3
1	1	5
2	1	1
2	1	5
3	1	1
3	1	2
3	1	5
4	1	3
4	1	5
5	1	2
5	1	3
5	1	5
6	1	1
6	1	2
6	1	3
6	1	4
6	1	5
7	1	5
8	1	1
8	1	3
8	1	5
9	1	1
10	4	1
10	4	2
11	1	1
11	1	2
11	1	3
12	2	1
12	3	1
12	2	3
12	2	4
12	2	2
12	3	2
12	2	5
12	3	5
\.


--
-- Name: operation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: davejohnson
--

SELECT pg_catalog.setval('operation_id_seq', 4, true);


--
-- Name: property_id_seq; Type: SEQUENCE SET; Schema: public; Owner: davejohnson
--

SELECT pg_catalog.setval('property_id_seq', 5, true);


--
-- Name: structure_id_seq; Type: SEQUENCE SET; Schema: public; Owner: davejohnson
--

SELECT pg_catalog.setval('structure_id_seq', 17, true);


--
-- Name: operation operation_name_key; Type: CONSTRAINT; Schema: public; Owner: davejohnson
--

ALTER TABLE ONLY operation
    ADD CONSTRAINT operation_name_key UNIQUE (name);


--
-- Name: operation operation_pkey; Type: CONSTRAINT; Schema: public; Owner: davejohnson
--

ALTER TABLE ONLY operation
    ADD CONSTRAINT operation_pkey PRIMARY KEY (id);


--
-- Name: property property_name_key; Type: CONSTRAINT; Schema: public; Owner: davejohnson
--

ALTER TABLE ONLY property
    ADD CONSTRAINT property_name_key UNIQUE (name);


--
-- Name: property property_pkey; Type: CONSTRAINT; Schema: public; Owner: davejohnson
--

ALTER TABLE ONLY property
    ADD CONSTRAINT property_pkey PRIMARY KEY (id);


--
-- Name: structure structure_name_key; Type: CONSTRAINT; Schema: public; Owner: davejohnson
--

ALTER TABLE ONLY structure
    ADD CONSTRAINT structure_name_key UNIQUE (name);


--
-- Name: structure_operation structure_operation_pkey; Type: CONSTRAINT; Schema: public; Owner: davejohnson
--

ALTER TABLE ONLY structure_operation
    ADD CONSTRAINT structure_operation_pkey PRIMARY KEY (structure_id, operation_id);


--
-- Name: structure_operation_property structure_operation_property_pkey; Type: CONSTRAINT; Schema: public; Owner: davejohnson
--

ALTER TABLE ONLY structure_operation_property
    ADD CONSTRAINT structure_operation_property_pkey PRIMARY KEY (structure_id, operation_id, property_id);


--
-- Name: structure structure_pkey; Type: CONSTRAINT; Schema: public; Owner: davejohnson
--

ALTER TABLE ONLY structure
    ADD CONSTRAINT structure_pkey PRIMARY KEY (id);


--
-- Name: structure_operation structure_operation_operation_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: davejohnson
--

ALTER TABLE ONLY structure_operation
    ADD CONSTRAINT structure_operation_operation_id_fkey FOREIGN KEY (operation_id) REFERENCES operation(id);


--
-- Name: structure_operation_property structure_operation_property_property_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: davejohnson
--

ALTER TABLE ONLY structure_operation_property
    ADD CONSTRAINT structure_operation_property_property_id_fkey FOREIGN KEY (property_id) REFERENCES property(id);


--
-- Name: structure_operation_property structure_operation_property_structure_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: davejohnson
--

ALTER TABLE ONLY structure_operation_property
    ADD CONSTRAINT structure_operation_property_structure_id_fkey FOREIGN KEY (structure_id, operation_id) REFERENCES structure_operation(structure_id, operation_id);


--
-- Name: structure_operation structure_operation_structure_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: davejohnson
--

ALTER TABLE ONLY structure_operation
    ADD CONSTRAINT structure_operation_structure_id_fkey FOREIGN KEY (structure_id) REFERENCES structure(id);


--
-- PostgreSQL database dump complete
--

