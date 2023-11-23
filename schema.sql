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
    "CodConsulta" SERIAL PRIMARY KEY NOT NULL,
    "ObsVet" VARCHAR(100) NOT NULL,
    "PrescVet" VARCHAR(100) NOT NULL   

);


CREATE TABLE IF NOT EXISTS "Animais"(
    "idAnimal" SERIAL PRIMARY KEY NOT NULL,
    "Idade" INTEGER NOT NULL,
    "Peso" INTEGER NOT NULL,
    "Raça" VARCHAR(20) NOT NULL,
    "Nome" VARCHAR(20) NOT NULL,
    "idAnimal" INTEGER NULL,
    "TamanhoBox" VARCHAR(20) NULL,
    
);


CREATE TABLE IF NOT EXISTS "Agendamento"(
    "NumProtocolo" SERIAL PRIMARY KEY NOT NULL,
    "CodConsulta" INTEGER PRIMARY KEY NOT NULL,
    "IdFunc" INTEGER NOT NULL,
    "DataAgend" VARCHAR(20) NOT NULL,
    "HoraAgend" VARCHAR(10) NOT NULL,
    

    FOREIGN KEY ("CodConsulta") REFERENCES "Consulta",
    FOREIGN KEY ("IdFunc") REFERENCES "Funcionarios"



);

CREATE TABLE IF NOT EXISTS "Tutor"(

);


CREATE TABLE IF NOT EXISTS "Possui"(

);