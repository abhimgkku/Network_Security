from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    trained_file_path: str
    test_file_path: str

@dataclass
class DataTransformationArtifact:
    pass

@dataclass
class DataValidationArtifact:
    pass

@dataclass
class ModelTrainerArtifact:
    pass

@dataclass
class ModelEvaluationArtifact:
    pass

@dataclass
class ModelPusherArtifact:
    pass

@dataclass
class ClassificationMatrixArtifact:
    pass
