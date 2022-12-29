'''
This is program to create any data in a hierarchial structure. It can be used for many applications and so the aim is to make if as modular and as flexible as possible.
We will use a system class and then use various class attributes and methods to create sub systems in a hierarchial fashion.
A system object will have sub-systems and any subsystem will also have the attributes of a system itself.
System attributes: SystemName, SystemID, SystemLevel, SystemDataType etc
System functions: CreateSystem, CreateSubSystems(one or many as per rerquirement),ModifySystem, SelectSystem(can be used to select a system or subsystem),AddSystem(This can use the create system function),DeleteSystem(this will first use the selectsystem function)
Class functions: These can be used for various tasks not directly related with system hierarchy but storage of data related to any sytemhierarchy. CreateDatabasefile, create tables, update database based on the changes done in a system. Thus the System functions would call class functions as per requriement. In fact creation of databae files and related tables as per requirement should be done whenever any new system is created and the user should provide inputs or defaults to be used.
'''
