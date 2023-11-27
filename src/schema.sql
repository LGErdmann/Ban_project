CREATE SCHEMA IF NOT EXISTS "main";

CREATE TABLE IF NOT EXISTS "Funcionario"(
    "id" SERIAL PRIMARY KEY NOT NULL,
    "Cargo" VARCHAR(50) NOT NULL,
    "Setor" VARCHAR(50) NOT NULL,
    "Telefone" VARCHAR(11) NOT NULL,
    "Email" VARCHAR(100) NOT NULL,
    "Salario" INTEGER NOT NULL,
    "Nome" VARCHAR(100) NOT NULL
);


CREATE TABLE IF NOT EXISTS "MedVet"(
    "idFunc" INTEGER PRIMARY KEY NOT NULL,
    "Turno" VARCHAR(50) NOT NULL,
    "Especialização" VARCHAR(100) NOT NULL,
    
    FOREIGN KEY ("idFunc") REFERENCES "Funcionario"

);



CREATE TABLE IF NOT EXISTS "Animal"(
    "idAnimal" SERIAL PRIMARY KEY NOT NULL,
    "Idade" INTEGER NOT NULL,
    "Peso" INTEGER NOT NULL,
    "Raça" VARCHAR(20) NOT NULL,
    "Nome" VARCHAR(20) NOT NULL,
    "NumBOX" INTEGER NULL,
    "TamanhoBox" VARCHAR(20) NULL
    
);

CREATE TABLE IF NOT EXISTS "Agendamento"(
    "NumProtocolo" SERIAL NOT NULL,
    "idAnimal" INTEGER NOT NULL,
    "IdFunc" INTEGER NOT NULL,
    "DataAgend" DATE UNIQUE NOT NULL,
    "HoraAgend" TIME UNIQUE NOT NULL,


    PRIMARY KEY ("NumProtocolo"),

    FOREIGN KEY ("idAnimal") REFERENCES "Animal",
    FOREIGN KEY ("IdFunc") REFERENCES "MedVet"



);

CREATE TABLE IF NOT EXISTS "Tutor"(
    "CPF" VARCHAR(11) PRIMARY KEY NOT NULL,
    "Email" VARCHAR(30) NOT NULL,
    "Endereço" VARCHAR(100) NOT NULL,
    "Nome" VARCHAR(30) NOT NULL,
    "Telefone" VARCHAR(11) NOT NULL
    

);


CREATE TABLE IF NOT EXISTS "Possui"(
    "CPF" VARCHAR(14) NOT NULL,
    "idAnimal" INTEGER NOT NULL,

    PRIMARY KEY ("CPF", "idAnimal"),

    FOREIGN KEY ("idAnimal") REFERENCES "Animal",
    FOREIGN KEY ("CPF") REFERENCES "Tutor"

);


CREATE TABLE IF NOT EXISTS "Consulta"(
    "NumProtocolo" INTEGER PRIMARY KEY NOT NULL,
    "ObsVet" VARCHAR(100) NOT NULL,
    "PrescVet" VARCHAR(100) NOT NULL,

    FOREIGN KEY ("NumProtocolo") REFERENCES "Agendamento"

);
