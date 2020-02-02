Create table ResearchParticipant (
    ResearchParticipant_ID          VARCHAR(20) NOT NULL,

    LifestyleSubject_ID             VARCHAR(20) NOT NULL,
    DemographicSubject_ID           VARCHAR(20) NOT NULL,
    PhysicalSubject_ID              VARCHAR(20) NOT NULL,

    BCG_ID                          VARCHAR(20) NOT NULL,
    Respiration_ID                  VARCHAR(20) NOT NULL,
    REM_ID                          VARCHAR(20) NOT NULL,
    DementiaLength_ID               VARCHAR(20) NOT NULL,
    DementiaRating_ID               VARCHAR(20) NOT NULL,
    PRIMARY KEY (ResearchParticipant_ID)
);

Create table LifeStyle (
    LifestyleSubject_ID             VARCHAR(20) NOT NULL,
    DaysofFitness                   VARCHAR(20) NOT NULL,
    AverageAlcoholicConsumption     INT         NOT NULL,
    AverageSleepHours               FLOAT       NOT NULL,
    RegularRecreationalDrugUse      FLOAT       NOT NULL,
    LaborHours                      FLOAT       NOT NULL,
    Smoker                          VARCHAR(1)  NOT NULL,
    FOREIGN KEY (LifestyleSubject_ID) REFERENCES ResearchParticipant (LifestyleSubject_ID),
    PRIMARY KEY (LifestyleSubject_ID)
);

Create table Demographic (
    DemographicSubject_ID           VARCHAR(20) NOT NULL,
    LevelofEducation                VARCHAR(20) NOT NULL,
    Gender                          VARCHAR(1)  NOT NULL,               
    Income                          FLOAT       NOT NULL,
    Age                             INT         NOT NULL,
    Ethnicity                       VARCHAR(20) NOT NULL,
    FOREIGN KEY (DemographicSubject_ID) REFERENCES ResearchParticipant (DemographicSubject_ID),
    PRIMARY KEY (DemographicSubject_ID)
);

Create table Physical (
    PhysicalSubject_ID              VARCHAR(20) NOT NULL,
    Height                          FLOAT(100)  NOT NULL,
    Weight                          FLOAT(100)  NOT NULL,
    HeartRate                       FLOAT(100)  NOT NULL,
    Diabetic                        VARCHAR(20) NOT NULL,
    Cancer                          VARCHAR(20) NOT NULL,
    FOREIGN KEY (PhysicalSubject_ID) REFERENCES ResearchParticipant (PhysicalSubject_ID),
    PRIMARY KEY (PhysicalSubject_ID)
);

Create table BCG (
    BCG_ID                          VARCHAR(20) NOT NULL,
    BCG_signal_segment              VARCHAR(20) NOT NULL,
    FOREIGN KEY (BCG_ID) REFERENCES ResearchParticipant (BCG_ID),
    PRIMARY KEY (BCG_ID)
);

Create table Respiration (
    Respiration_ID                  VARCHAR(20) NOT NULL,
    Respiration                     VARCHAR(20) NOT NULL,
    FOREIGN KEY (Respiration_ID) REFERENCES ResearchParticipant (Respiration_ID),
    PRIMARY KEY (Respiration_ID)
);

Create table REM (
    REM_ID                          VARCHAR(20) NOT NULL,
    REM_segment                     VARCHAR(20) NOT NULL,
    FOREIGN KEY (REM_ID) REFERENCES ResearchParticipant (REM_ID),
    PRIMARY KEY (REM_ID)
);

Create table Dementia_Length (
    DementiaLength_ID               VARCHAR(20) NOT NULL,
    Dementia_SegmentLength          FLOAT       NOT NULL,
    Max_DementiaLength              FLOAT       NOT NULL,
    Average_SegemntLength           FLOAT       NOT NULL,
    Total_SegmengtLength            FLOAT       NOT NULL,
    FOREIGN KEY (DementiaLength_ID) REFERENCES ResearchParticipant (DementiaLength_ID),
    PRIMARY KEY (DementiaLength_ID)
);

Create DementiaRating (
    DementiaRating_ID               VARCHAR(20) NOT NULL, 
    Dementia_SegemntRating          FLOAT       NOT NULL,
    Max_DementiaRating              FLOAT       NOT NULL,
    Average_DementiaRating          FLOAT       NOT NULL,
    FOREIGN KEY (DementiaRating_ID) REFERENCES ResearchParticipant (DementiaRating_ID),
    PRIMARY KEY (DementiaRating_ID)
);
