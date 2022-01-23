from app import db


class Library_Spectra(db.Model):
    __tablename__ = 'library_spectra'
    id = db.Column(db.Integer, primary_key = True)
    mz = db.Column(db.Float)
    i = db.Column(db.Float)
    other= db.Column(db.String, nullable=True)
    library_spectra_meta_id= db.Column(db.Integer, db.ForeignKey('library_spectra_meta.id'))

    def __init__(self, id, mz, i, other, library_spectra_meta_id):
        self.id = id
        self.mz = mz
        self.i= i
        self.other= other
        self.library_spectra_meta_id= library_spectra_meta_id



class Library_Spectra_annotation(db.Model):
    __tablename__ = 'library_spectra_annotation'
    id = db.Column(db.Integer, primary_key = True)
    mz = db.Column(db.Float)
    tentative_formula = db.Column(db.String)
    mass_error = db.Column(db.Float)
    library_spectra_meta_id= db.Column(db.Integer, db.ForeignKey('library_spectra_meta.id'))

    def __init__(self, id, mz, tentative_formula, mass_error, library_spectra_meta_id):
        self.id = id
        self.mz = mz
        self.tentative_formula = tentative_formula
        self.mass_error = mass_error
        self.library_spectra_meta_id= library_spectra_meta_id


class Library_spectra_meta(db.Model):
    __tablename__ = 'library_spectra_meta'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    collision_energy = db.Column(db.String)
    ms_level= db.Column(db.Float)
    accession = db.Column(db.String)
    resolution = db.Column(db.String)
    polarity = db.Column(db.Integer)
    fragmentation_type = db.Column(db.String)
    precursor_mz = db.Column(db.Float)
    precursor_type = db.Column(db.String)
    instrument_type = db.Column(db.String)
    instrument = db.Column(db.String)
    copyright = db.Column(db.String)
    column = db.Column(db.String)
    mass_accuracy = db.Column(db.Float)
    mass_error = db.Column(db.Float)
    origin = db.Column(db.String)
    splash = db.Column(db.String)
    retention_index = db.Column(db.Float)
    retention_time = db.Column(db.Float)
    library_spectra_source_id= db.Column(db.Integer)
    inchikey_id = db.Column(db.String, db.ForeignKey('metab_compound.inchikey_id'))


    def __init__(self, id, name, collision_energy, ms_level, accession, resolution, polarity, fragmentation_type, precursor_mz, precursor_type, instrument_type, instrument, copyright, column, mass_accuracy, mass_error, origin, splash, retention_index, retention_time, library_spectra_meta_id, inchikey_id):
        self.id = id
        self.name = name
        self.collision_energy = collision_energy
        self.ms_level= ms_level
        self.accession = accession
        self.resolution = resolution
        self.polarity = polarity
        self.fragmentation_type = fragmentation_type
        self.precursor_mz = precursor_mz
        self.precursor_type = precursor_type
        self.instrument_type = instrument_type
        self.instrument = instrument
        self.copyright = copyright
        self.column = column
        self.mass_accuracy = mass_accuracy
        self.mass_error = mass_error
        self.origin = origin
        self.splash = splash
        self.retention_index = retention_index
        self.retention_time = retention_time
        self.library_spectra_meta_id= library_spectra_meta_id
        self.inchikey_id = inchikey_id



class Library_spectra_source(db.Model):
    __tablename__ = 'library_spectra_source'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    created_at = db.Column(db.Date)
    parsing_software = db.Column(db.String)

    def __init__(self, id, name, created_at, parsing_software):
        self.id = id
        self.name = name
        self.created_at = created_at
        self.parsing_software = parsing_software



class Metab_compound(db.Model):
    __tablename__ = 'metab_compound'
    inchikey_id = db.Column(db.String, primary_key = True)
    name = db.Column(db.String)
    pubchem_id = db.Column(db.String)
    chemspider_id = db.Column(db.String)
    other_names = db.Column(db.String)
    exact_mass = db.Column(db.Float)
    molecular_formula = db.Column(db.String)
    molecular_weight = db.Column(db.Float)
    compound_class = db.Column(db.String)
    smiles = db.Column(db.String)
    created_at= db.Column(db.Date)
    updated_at= db.Column(db.Date)

    def __init__(self, inchikey_id, name, pubchem_id, chemspider_id, other_names, exact_mass, molecular_formula, molecular_weight, compound_class, smiles, created_at, updated_at):
        self.inchikey_id = inchikey_id
        self.name = name
        self.pubchem_id = pubchem_id
        self.chemspider_id = chemspider_id
        self.other_names = other_names
        self.exact_mass = exact_mass
        self.molecular_formula = molecular_formula
        self.molecular_weight = molecular_weight
        self.compound_class = compound_class
        self.smiles = smiles
        self.created_at= created_at
        self.updated_at= updated_at
