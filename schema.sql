BEGIN;


CREATE TABLE IF NOT EXISTS "Funcionarios"(
    "id" SERIAL PRIMARY KEY NOT NULL,
    "Cargo" VARCHAR(50) NOT NULL,
    "Setor" VARCHAR(50) NOT NULL,
    "Telefone" VARCHAR(20) NOT NULL,
    "Email" VARCHAR(100) NOT NULL,
    "Salário" INTEGER NOT NULL,
    "Nome" VARCHAR(100) NOT NULL
);


CREATE TABLE IF NOT EXISTS "MedVet"(
    "idFunc" INTEGER PRIMARY KEY NOT NULL,
    "Turno" VARCHAR(50) NOT NULL,
    "Especialização" VARCHAR(100) NOT NULL,
    
    FOREIGN KEY ("idFunc") REFERENCES "Funcionarios"

);


CREATE TABLE IF NOT EXISTS "Consulta"(

);


CREATE TABLE IF NOT EXISTS "Animais"(

);


CREATE TABLE IF NOT EXISTS "Agendamento"(

);

CREATE TABLE IF NOT EXISTS "Tutor"(

);


CREATE TABLE IF NOT EXISTS "Possui"(

);