# 📘 Database Schema (Tables + Selected Views)


## 🧱 TABLES – Schema `dbo`

### TABLE: `dbo.Aircraft`

```sql
CREATE TABLE [dbo].[Aircraft] (
  [AircraftId] INTEGER NOT NULL,
  [TailNumber] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [AircraftTypeId] INTEGER,
  [CommissioningDate] DATETIME,
  [LastCheck] DATETIME,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
AircraftId	TailNumber	AircraftTypeId	CommissioningDate	LastCheck	TenantId
1	VT-AYD	1	2022-01-01 00:00:00	None	1
6	VT-HYD	1	2022-01-05 00:00:00	None	1

```

### TABLE: `dbo.AircraftType`

```sql
CREATE TABLE [dbo].[AircraftType] (
  [AircraftTypeId] INTEGER NOT NULL,
  [AircraftType] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [AircraftMake] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [SeatConfiguration] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Quantity] INTEGER,
  [Description] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [PassengerCapacity] INTEGER,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
AircraftTypeId	AircraftType	AircraftMake	SeatConfiguration	Quantity	Description	PassengerCapacity	TenantId
1	A320-B06	A320-B06	Standard	1	A320 DESC	25	1
7	A320-B06	A320-B06	Standard	1	A320 DESC	25	28
8	c1	n1	Standard	1	des1	2	1

```

### TABLE: `dbo.AirportMaster`

```sql
CREATE TABLE [dbo].[AirportMaster] (
  [AirportId] INTEGER NOT NULL,
  [AirportCode] NVARCHAR(3) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [AirportName] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [City] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [CountryId] INTEGER,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
AirportId	AirportCode	AirportName	City	CountryId	TenantId
1	RUH	Riyadh International Airport	Riyadh	194	1
2	JED	Jeddah International Airport	Jeddah	194	1
3	DXB	Dubai International Airport - T3	Dubai	234	1

```

### TABLE: `dbo.Asset`

```sql
CREATE TABLE [dbo].[Asset] (
  [AssetId] INTEGER NOT NULL,
  [AssetNumber] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Description] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [CategoryId] INTEGER,
  [GroupId] INTEGER,
  [LocationId] INTEGER,
  [ParentId] INTEGER,
  [PONumber] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [DateRecd] DATETIME,
  [Value] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Quantity] INTEGER,
  [OwnerId] INTEGER,
  [DepartmentId] INTEGER,
  [DepreciationMethod] INTEGER,
  [CheckoutStatus] INTEGER,
  [CheckoutDate] DATETIME,
  [ReturnDate] DATETIME,
  [TagNumber] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [SerialNumber] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TaggedOn] DATETIME,
  [AssetCondition] INTEGER,
  [DepreciationStatus] INTEGER,
  [WarrantyStatus] INTEGER,
  [WarrantyDate] DATETIME,
  [WarrantyPeriod] INTEGER,
  [MaintenancePeriod] INTEGER,
  [ReplacedAssetId] INTEGER,
  [ReplacedOn] DATETIME,
  [ReplacedBy] INTEGER,
  [AssetStatus] INTEGER,
  [TenantId] INTEGER NOT NULL,
  [CreatedOn] DATETIME,
  [CreatedBy] INTEGER,
  [MakeId] INTEGER,
  [ModelId] INTEGER,
  [DesignId] INTEGER,
  [xCoordinate] INTEGER,
  [yCoordinate] INTEGER,
  [mapid] INTEGER
);
```
Sample Rows:
```text
AssetId	AssetNumber	Description	CategoryId	GroupId	LocationId	ParentId	PONumber	DateRecd	Value	Quantity	OwnerId	DepartmentId	DepreciationMethod	CheckoutStatus	CheckoutDate	ReturnDate	TagNumber	SerialNumber	TaggedOn	AssetCondition	DepreciationStatus	WarrantyStatus	WarrantyDate	WarrantyPeriod	MaintenancePeriod	ReplacedAssetId	ReplacedOn	ReplacedBy	AssetStatus	TenantId	CreatedOn	CreatedBy	MakeId	ModelId	DesignId	xCoordinate	yCoordinate	mapid
1	AST01	Asset 01	2	8	400	None	PN01	2021-10-16 13:55:00	100 AED	1	1	4	1	2	2021-11-01 16:15:32.570000	2021-11-02 00:00:00	TN01	SN01	None	1	2	2	2021-10-31 00:00:00	None	None	None	None	None	2	1	2021-10-16 13:55:00	1	None	None	None	None	None	None
3	AST02	Asset 02	2	8	3	None	PN01	2021-10-16 13:55:00	100 AED	1	1	4	1	1	2022-01-05 09:19:53.680000	None	TN02	SN02	None	2	1	1	2021-10-31 00:00:00	None	None	None	None	None	2	1	2021-10-16 13:55:00	1	None	None	None	None	None	None
4	AST03	Asset 03	2	8	4	None	PN03	2021-10-18 16:35:00	300 AED	3	1	2	1	2	2022-01-05 09:20:17.397000	2022-01-08 00:00:00	TN03	SN03	None	2	1	2	2021-10-27 00:00:00	None	None	None	None	None	3	1	2021-10-18 16:34:13.483000	1	None	None	None	None	None	None

```

### TABLE: `dbo.AssetDepreciation`

```sql
CREATE TABLE [dbo].[AssetDepreciation] (
  [Id] INTEGER NOT NULL,
  [AssetId] INTEGER NOT NULL,
  [DepreciationDate] DATETIME,
  [AssetCost] DECIMAL(18, 2),
  [DepreciatedValue] DECIMAL(18, 2)
);
```
Sample Rows:
```text
Id	AssetId	DepreciationDate	AssetCost	DepreciatedValue
1	1	2021-10-16 13:55:00	100.00	100.00
2	3	2021-09-16 13:55:00	100.00	100.00
3	4	2020-10-16 13:55:00	100.00	100.00

```

### TABLE: `dbo.AssetHistory`

```sql
CREATE TABLE [dbo].[AssetHistory] (
  [AssetHistoryId] INTEGER NOT NULL,
  [AssetId] INTEGER,
  [Type] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Description] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [CreatedOn] DATETIME,
  [CreatedBy] INTEGER
);
```
Sample Rows:
```text
AssetHistoryId	AssetId	Type	Description	CreatedOn	CreatedBy
1	1	Created	Created new asset - <a href='javascript:void(0)' onclick='onView(4)'> View </a>.	2021-10-16 13:58:14.957000	1
2	3	Created	Created new asset.	2021-10-16 14:14:26.807000	1
3	3	Make Copy	Copy asset from - <a href='/Asset/AssetHistory?asset=1'> AST01 </a>.	2021-10-16 14:16:14.387000	1

```

### TABLE: `dbo.AutoIncrement`

```sql
CREATE TABLE [dbo].[AutoIncrement] (
  [AutoIncrementId] INTEGER NOT NULL,
  [IncrementNumber] INTEGER NOT NULL,
  [Prefix] NVARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [PadNumber] INTEGER,
  [Entity] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL
);
```
Sample Rows:
```text
AutoIncrementId	IncrementNumber	Prefix	PadNumber	Entity
1	14	TCKN-	5	TicketNumber
2	3	TK-	5	ToolKit
3	9	TR-	5	ToolReservation

```

### TABLE: `dbo.BagHistory`

```sql
CREATE TABLE [dbo].[BagHistory] (
  [HistoryId] INTEGER NOT NULL,
  [BagId] INTEGER NOT NULL,
  [ScanPointId] INTEGER,
  [ScanTime] DATETIME,
  [ScanUserId] INTEGER
);
```
Sample Rows:
```text
HistoryId	BagId	ScanPointId	ScanTime	ScanUserId
444	72	19	2022-12-05 13:41:19.580000	1
445	73	19	2022-12-05 13:41:20.323000	1
446	75	19	2022-12-05 13:41:21.063000	1

```

### TABLE: `dbo.BagList`

```sql
CREATE TABLE [dbo].[BagList] (
  [Id] INTEGER NOT NULL,
  [BagId] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [PassengerId] INTEGER,
  [CurrentStatus] INTEGER,
  [LastSeenAt] INTEGER,
  [LastSeenTime] DATETIME,
  [TenantId] INTEGER NOT NULL,
  [Weight] FLOAT
);
```
Sample Rows:
```text
Id	BagId	PassengerId	CurrentStatus	LastSeenAt	LastSeenTime	TenantId	Weight
72	E2004078370D0123254014D1	1	3	3	2022-12-06 13:35:16.420000	1	40.0
73	E2004078370D0113254014B4	1	3	3	2022-12-06 13:22:37.890000	1	10.0
75	E2004078370D014925401502	1	3	3	2022-12-06 15:38:23.883000	1	20.0

```

### TABLE: `dbo.BedAllocation`

```sql
CREATE TABLE [dbo].[BedAllocation] (
  [BedAllocationID] INTEGER NOT NULL,
  [WardLocationID] INTEGER,
  [BedID] INTEGER,
  [PatientID] INTEGER,
  [StartFrom] DATETIME,
  [EndAt] DATETIME,
  [isActive] BIT,
  [CreatedBy] INTEGER,
  [CreatedOn] DATETIME,
  [OTScheduleID] INTEGER,
  [UpdatedBy] INTEGER,
  [UpdatedOn] DATETIME
);
```
Sample Rows:
```text
BedAllocationID	WardLocationID	BedID	PatientID	StartFrom	EndAt	isActive	CreatedBy	CreatedOn	OTScheduleID	UpdatedBy	UpdatedOn
1105	74	5	331	2020-03-17 09:45:00	2020-03-17 12:55:55.590000	False	1253	2020-03-17 09:43:10.850000	332	1102	2020-03-17 12:55:55.590000
1106	74	27	333	2020-03-17 12:00:00	2020-03-23 08:41:53.470000	False	1253	2020-03-17 09:44:11.037000	334	1317	2020-03-23 08:41:53.470000
1107	74	2	328	2020-03-17 06:00:00	None	False	1306	2020-03-17 15:18:10.337000	329	1306	2020-03-17 15:19:05.013000

```

### TABLE: `dbo.BinMaster`

```sql
CREATE TABLE [dbo].[BinMaster] (
  [BinId] INTEGER NOT NULL,
  [BinCode] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [RackCode] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [AisleCode] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Levels] INTEGER,
  [Dimension] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [WeightCapacity] INTEGER,
  [Status] INTEGER,
  [BinTypeId] INTEGER,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
BinId	BinCode	RackCode	AisleCode	Levels	Dimension	WeightCapacity	Status	BinTypeId	TenantId
1	ZA-R1-L1-01	R1	ZA	1	12*12*12	1000	1	21	1
2	ZA-R1-L2-01	R1	ZA	2	12x12x12	1000	2	24	1
3	ZA-R1-L3-01	R1	ZA	3	12x12x12	1000	2	21	1

```

### TABLE: `dbo.BLETagAllocation`

```sql
CREATE TABLE [dbo].[BLETagAllocation] (
  [BLEAllocationID] INTEGER NOT NULL,
  [BLETagID] INTEGER NOT NULL,
  [OTScheduleID] INTEGER,
  [PatientID] INTEGER,
  [StaffID] INTEGER,
  [AssignedOn] DATETIME NOT NULL,
  [AssignedByUserID] INTEGER,
  [IsCancelled] INTEGER,
  [CancelledBy] INTEGER,
  [CancelledOn] DATETIME,
  [IsActive] BIT NOT NULL,
  [AllocationType] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ReferenceID] INTEGER,
  [isVerified] BIT NOT NULL,
  [VerifiedOn] DATETIME,
  [VerifiedBy] INTEGER
);
```
Sample Rows:
```text
BLEAllocationID	BLETagID	OTScheduleID	PatientID	StaffID	AssignedOn	AssignedByUserID	IsCancelled	CancelledBy	CancelledOn	IsActive	AllocationType	ReferenceID	isVerified	VerifiedOn	VerifiedBy
96	265	332	331	None	2020-03-17 08:51:06.507000	None	1	1102	2020-04-02 09:32:43.937000	True	None	None	False	None	None
97	355	333	332	None	2020-03-17 09:11:32.493000	None	1	1102	2020-03-17 08:57:23.160000	True	None	None	False	None	None
98	354	334	333	None	2020-03-17 10:47:43.940000	None	1	1102	2020-04-02 09:32:35.513000	True	None	None	False	None	None

```

### TABLE: `dbo.BLETags`

```sql
CREATE TABLE [dbo].[BLETags] (
  [BLETagID] INTEGER NOT NULL,
  [OrganizationId] INTEGER,
  [TagNumber] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [IsAssigned] INTEGER NOT NULL,
  [RequiresSantization] INTEGER NOT NULL,
  [TagType] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [IsActive] BIT NOT NULL,
  [LastSeen] DATETIME,
  [BatteryLevel] INTEGER,
  [LastSeenLocation] INTEGER,
  [SerialNumber] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [LastSeenTemp] DATETIME,
  [LastSeenLocTemp] INTEGER,
  [BatteryTLM] INTEGER,
  [BatteryInfo] INTEGER,
  [BatteryMB] INTEGER,
  [NotifiedDate] DATETIME
);
```
Sample Rows:
```text
BLETagID	OrganizationId	TagNumber	IsAssigned	RequiresSantization	TagType	IsActive	LastSeen	BatteryLevel	LastSeenLocation	SerialNumber	LastSeenTemp	LastSeenLocTemp	BatteryTLM	BatteryInfo	BatteryMB	NotifiedDate
14	1	AC233F53690B	1	2	StaffID	True	2020-09-01 08:16:20.310000	0	66	NMCCB146	None	None	None	None	None	None
15	1	AC233F53688A	1	2	StaffID	True	2022-03-16 08:09:58.947000	0	66	NMCCB17	None	None	None	None	None	None
16	1	AC233F536885	1	2	StaffID	True	2022-03-16 08:59:16.860000	0	209	NMCCB12	None	None	None	None	None	None

```

### TABLE: `dbo.BusinessRuleLocation`

```sql
CREATE TABLE [dbo].[BusinessRuleLocation] (
  [BRLId] INTEGER NOT NULL,
  [BusinessRuleId] INTEGER,
  [LocationId] INTEGER
);
```
Sample Rows:
```text
BRLId	BusinessRuleId	LocationId
1	1	3

```

### TABLE: `dbo.BusinessRuleMaster`

```sql
CREATE TABLE [dbo].[BusinessRuleMaster] (
  [BusinessRuleId] INTEGER NOT NULL,
  [Name] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [RuleType] INTEGER,
  [MinMaxValue] INTEGER,
  [IsValidDate] BIT,
  [ApplicableStartDate] DATETIME,
  [ApplicableEndDate] DATETIME,
  [IsValidTime] BIT,
  [ApplicableStartTime] INTEGER,
  [ApplicableEndTime] INTEGER,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
BusinessRuleId	Name	RuleType	MinMaxValue	IsValidDate	ApplicableStartDate	ApplicableEndDate	IsValidTime	ApplicableStartTime	ApplicableEndTime	TenantId
1	BR01	3	None	False	None	None	True	1245	1245	1
2	Name	1	12	False	None	None	False	None	None	1
4	BSR1	1	2	True	2001-05-01 00:00:00	2001-10-01 00:00:00	True	450	570	1

```

### TABLE: `dbo.BusinessUnits`

```sql
CREATE TABLE [dbo].[BusinessUnits] (
  [UnitId] INTEGER NOT NULL,
  [Name] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [ParentUnitId] INTEGER
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `dbo.CargoMoveHistory`

```sql
CREATE TABLE [dbo].[CargoMoveHistory] (
  [MoveId] INTEGER NOT NULL,
  [CargoId] INTEGER,
  [TransactionType] INTEGER,
  [TimeStamp] DATETIME,
  [Description] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS"
);
```
Sample Rows:
```text
MoveId	CargoId	TransactionType	TimeStamp	Description
1	1	1	2022-01-19 15:43:18.747000	New cargo created.
2	2	1	2022-01-20 10:38:12.733000	New cargo created.
3	2	5	2022-01-21 13:21:34.533000	Packed to 10001

```

### TABLE: `dbo.CargoPackage`

```sql
CREATE TABLE [dbo].[CargoPackage] (
  [CargoId] INTEGER NOT NULL,
  [CargoNumber] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Date] DATETIME,
  [AWB] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [MAWB] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [HAWB] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [SenderName] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [SenderAddress1] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [SenderAddress2] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [SenderCity] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [SenderCountry] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [SenderPhone] NVARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ConsigneeName] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ConsigneeAddress1] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ConsigneeAddress2] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ConsigneeCity] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ConsigneeCountry] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ConsigneePhone] NVARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Piece] NVARCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Status] INTEGER,
  [FlightNumber] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [FlightDate] DATETIME,
  [FlightDestination] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [BinId] INTEGER,
  [Dimension] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Weight] FLOAT,
  [PalletId] INTEGER,
  [CargoTypeId] INTEGER,
  [WSId] INTEGER,
  [TagNo] NVARCHAR(24) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [InvStatus] NVARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
CargoId	CargoNumber	Date	AWB	MAWB	HAWB	SenderName	SenderAddress1	SenderAddress2	SenderCity	SenderCountry	SenderPhone	ConsigneeName	ConsigneeAddress1	ConsigneeAddress2	ConsigneeCity	ConsigneeCountry	ConsigneePhone	Piece	Status	FlightNumber	FlightDate	FlightDestination	BinId	Dimension	Weight	PalletId	CargoTypeId	WSId	TagNo	InvStatus	TenantId
1	CARGO-00001	2022-01-20 00:00:00	AWB-01	MAWB-01	HAWB-01	Sender Name 01	Sender Addess1 01	Sender Addess2 01	Sender City 01	Sender Country 01	1245789630	Consignee Name 01	Consignee Address1 01	Consignee Address2 01	Consignee City	Consignee Country 01	1234567890	5	4	FN-01-5502	2022-01-20 00:00:00	Dubai	None	12*12*12	25.0	1	25	1	TAG01	INV-1	1
2	CARGO-00002	2022-01-20 00:00:00	AWB-01	MAWB-01	HAWB-01	Sender Name 01	Sender Addess1 01	Sender Addess2 01	Sender City 01	Sender Country 01	1245789630	Consignee Name 01	Consignee Address1 01	Consignee Address2 01	Consignee City	Consignee Country 01	1234567890	5	5	FN-01-5502	2022-01-20 00:00:00	Dubai	None	12*12*12	25.0	None	25	1	None	None	1
4	CARGO-00004	2001-05-01 00:00:00	AWB1	MAWB1	HAWB1	Sender1	Dilsuk	None	hyd	ind	1212121212	Consignee1	dubai	None	dubai	dubai	1212121212	P1	5	F001	2022-10-22 00:00:00	Manager	7	None	None	None	1155	3	None	None	1

```

### TABLE: `dbo.CarrierMaster`

```sql
CREATE TABLE [dbo].[CarrierMaster] (
  [CarrierId] INTEGER NOT NULL,
  [CarrierCode] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [CarrierName] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
CarrierId	CarrierCode	CarrierName	TenantId
1	EK	Emirates	1
2	G9	Air Arabia	1
3	SRA	Saudi Royal Aviation	1

```

### TABLE: `dbo.Contacts`

```sql
CREATE TABLE [dbo].[Contacts] (
  [ContactId] INTEGER NOT NULL,
  [Title] NVARCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [FirstName] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [LastName] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [Email] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [IdentityNo] NVARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [UserId] INTEGER
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `dbo.Countries`

```sql
CREATE TABLE [dbo].[Countries] (
  [CountryId] INTEGER NOT NULL,
  [CountryName] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TwoCharCountryCode] NVARCHAR(2) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ThreeCharCountryCode] NVARCHAR(3) COLLATE "SQL_Latin1_General_CP1_CI_AS"
);
```
Sample Rows:
```text
CountryId	CountryName	TwoCharCountryCode	ThreeCharCountryCode
1	Afghanistan	AF	AFG
2	Aland Islands	AX	ALA
3	Albania	AL	ALB

```

### TABLE: `dbo.DashboardWidget`

```sql
CREATE TABLE [dbo].[DashboardWidget] (
  [WidgetId] INTEGER NOT NULL,
  [HtmlId] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [WidgetType] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Description] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS"
);
```
Sample Rows:
```text
WidgetId	HtmlId	WidgetType	Description
1	AssetCount	Count	Asset Count
2	AssetLastWeekCount	Count	Asset Last Week Count
3	CustomerCount	Count	Customer Count

```

### TABLE: `dbo.DataAuditLog`

```sql
CREATE TABLE [dbo].[DataAuditLog] (
  [LogId] INTEGER NOT NULL,
  [LogType] SMALLINT NOT NULL,
  [LogDate] DATETIME NOT NULL,
  [UserId] INTEGER,
  [TableName] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [RecordId] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [FieldName] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [OldValue] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [NewValue] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS"
);
```
Sample Rows:
```text
LogId	LogType	LogDate	UserId	TableName	RecordId	FieldName	OldValue	NewValue
1	1	2021-11-26 08:11:12.497000	1	[dbo].[Asset]	9	AssetId	None	9
2	1	2021-11-26 08:11:12.497000	1	[dbo].[Asset]	9	AssetNumber	None	AST05.1
3	1	2021-11-26 08:11:12.497000	1	[dbo].[Asset]	9	Description	None	Asset 05.1

```

### TABLE: `dbo.Department`

```sql
CREATE TABLE [dbo].[Department] (
  [DepartmentId] INTEGER NOT NULL,
  [DepartmentCode] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [DepartmentName] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
DepartmentId	DepartmentCode	DepartmentName	TenantId
1	DEPT01	Department 01	1
2	DEPT02	Department 02	1
3	DEPT03	Department03	1

```

### TABLE: `dbo.Exceptions`

```sql
CREATE TABLE [dbo].[Exceptions] (
  [Id] BIGINT NOT NULL,
  [GUID] UNIQUEIDENTIFIER NOT NULL,
  [ApplicationName] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [MachineName] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [CreationDate] DATETIME NOT NULL,
  [Type] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [IsProtected] BIT NOT NULL,
  [Host] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Url] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [HTTPMethod] NVARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [IPAddress] NVARCHAR(40) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Source] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Message] NVARCHAR(1000) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Detail] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [StatusCode] INTEGER,
  [SQL] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [DeletionDate] DATETIME,
  [FullJson] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ErrorHash] INTEGER,
  [DuplicateCount] INTEGER NOT NULL
);
```
Sample Rows:
```text
Id	GUID	ApplicationName	MachineName	CreationDate	Type	IsProtected	Host	Url	HTTPMethod	IPAddress	Source	Message	Detail	StatusCode	SQL	DeletionDate	FullJson	ErrorHash	DuplicateCount
1	07cca033-1674-4657-8d72-98eec3cfbf4d	TrackIT.Web	WIN-U29L07RA6MG	2024-04-04 11:08:27.493000	System.InvalidProgramException	False	entrackx1.trackit.aero	/DynJS.axd/ColumnsBundle.js	GET	115.112.167.238	Serenity.Net.Entity	TrackIT.GSE.Columns.AssetTripsColumns has a [BasedOnRow(typeof(TrackIT.GSE.Entities.AssetTripsRow), CheckNames = true)] attribute but its 'Operator' property doesn't have a matching field with same property / field name in the row.

Please check if property is named correctly.

To remove this validation you may set CheckNames to false on [BasedOnRow] attribute.

To disable check for this specific property add a [IgnoreName] attribute to the property itself.	System.InvalidProgramException: TrackIT.GSE.Columns.AssetTripsColumns has a [BasedOnRow(typeof(TrackIT.GSE.Entities.AssetTripsRow), CheckNames = true)] attribute but its 'Operator' property doesn't have a matching field with same property / field name in the row.

Please check if property is named correctly.

To remove this validation you may set CheckNames to false on [BasedOnRow] attribute.

To disable check for this specific property add a [IgnoreName] attribute to the property itself.
   at Serenity.PropertyGrid.DefaultPropertyItemProvider.GetPropertyItemsFor(Type type) in C:\Sandbox\StartSharp\Serenity\src\Serenity.Net.Entity\PropertyGrid\DefaultPropertyItemProvider.cs:line 78
   at Serenity.Web.PropertyItemsScript.GetScript() in C:\Sandbox\StartSharp\Serenity\src\Serenity.Net.Web\DynamicScript\PropertyEditor\PropertyItemsScript.cs:line 55
   at Serenity.Web.ConcatenatedScript.GetScript() in C:\Sandbox\StartSharp\Serenity\src\Serenity.Net.Web\DynamicScript\DynamicScriptTypes\ConcatenatedScript.cs:line 33
   at Serenity.Web.DynamicScriptManager.<>c__DisplayClass16_0.<EnsureScriptContent>g__factory|0() in C:\Sandbox\StartSharp\Serenity\src\Serenity.Net.Web\DynamicScript\DynamicScript\DynamicScriptManager.cs:line 132
   at Serenity.MemoryCacheExtensions.Get[TItem](IMemoryCache cache, Object cacheKey, TimeSpan expiration, Func`1 loader) in C:\Sandbox\StartSharp\Serenity\src\Serenity.Net.Core\Caching\MemoryCacheExtensions.cs:line 64
   at Serenity.Web.DynamicScriptManager.<>c__DisplayClass16_0.<EnsureScriptContent>g__getOrCreate|1() in C:\Sandbox\StartSharp\Serenity\src\Serenity.Net.Web\DynamicScript\DynamicScript\DynamicScriptManager.cs:line 141
   at Serenity.Web.DynamicScriptManager.EnsureScriptContent(String name, IDynamicScript script) in C:\Sandbox\StartSharp\Serenity\src\Serenity.Net.Web\DynamicScript\DynamicScript\DynamicScriptManager.cs:line 136
   at Serenity.Web.DynamicScriptManager.ReadScriptContent(String name) in C:\Sandbox\StartSharp\Serenity\src\Serenity.Net.Web\DynamicScript\DynamicScript\DynamicScriptManager.cs:line 199
   at Serenity.Web.Middleware.DynamicScriptMiddleware.ReturnScript(HttpContext context, String scriptKey, String contentType)
   at Microsoft.AspNetCore.Authorization.AuthorizationMiddleware.Invoke(HttpContext context)
   at Microsoft.AspNetCore.Authentication.AuthenticationMiddleware.Invoke(HttpContext context)
   at StackExchange.Exceptional.ExceptionalMiddleware.Invoke(HttpContext context)

Full Trace:

   at StackExchange.Exceptional.ExceptionalMiddleware.Invoke(HttpContext context)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at StackExchange.Exceptional.ExceptionalMiddleware.Invoke(HttpContext context)
   at Microsoft.AspNetCore.HttpsPolicy.HttpsRedirectionMiddleware.Invoke(HttpContext context)
   at Microsoft.AspNetCore.Diagnostics.DeveloperExceptionPageMiddleware.Invoke(HttpContext context)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at Microsoft.AspNetCore.Diagnostics.DeveloperExceptionPageMiddleware.Invoke(HttpContext context)
   at Microsoft.AspNetCore.Localization.RequestLocalizationMiddleware.Invoke(HttpContext context)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at Microsoft.AspNetCore.Localization.RequestLocalizationMiddleware.Invoke(HttpContext context)
   at Microsoft.AspNetCore.StaticFiles.StaticFileMiddleware.Invoke(HttpContext context)
   at Swashbuckle.AspNetCore.SwaggerUI.SwaggerUIMiddleware.Invoke(HttpContext httpContext)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at Swashbuckle.AspNetCore.SwaggerUI.SwaggerUIMiddleware.Invoke(HttpContext httpContext)
   at Swashbuckle.AspNetCore.Swagger.SwaggerMiddleware.Invoke(HttpContext httpContext, ISwaggerProvider swaggerProvider)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at Swashbuckle.AspNetCore.Swagger.SwaggerMiddleware.Invoke(HttpContext httpContext, ISwaggerProvider swaggerProvider)
   at Microsoft.AspNetCore.Cors.Infrastructure.CorsMiddleware.Invoke(HttpContext context, ICorsPolicyProvider corsPolicyProvider)
   at NWebsec.AspNetCore.Middleware.Middleware.MiddlewareBase.Invoke(HttpContext context)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at NWebsec.AspNetCore.Middleware.Middleware.MiddlewareBase.Invoke(HttpContext context)
   at NWebsec.AspNetCore.Middleware.Middleware.MiddlewareBase.Invoke(HttpContext context)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at NWebsec.AspNetCore.Middleware.Middleware.MiddlewareBase.Invoke(HttpContext context)
   at App.Metrics.AspNetCore.Tracking.Middleware.ApdexMiddleware.MeasureTransaction(HttpContext context)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at App.Metrics.AspNetCore.Tracking.Middleware.ApdexMiddleware.MeasureTransaction(HttpContext context)
   at App.Metrics.AspNetCore.Tracking.Middleware.PerRequestTimerMiddleware.TimeTransaction(HttpContext context)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at App.Metrics.AspNetCore.Tracking.Middleware.PerRequestTimerMiddleware.TimeTransaction(HttpContext context)
   at App.Metrics.AspNetCore.Tracking.Middleware.RequestTimerMiddleware.TimeTransaction(HttpContext context)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at App.Metrics.AspNetCore.Tracking.Middleware.RequestTimerMiddleware.TimeTransaction(HttpContext context)
   at App.Metrics.AspNetCore.Tracking.Middleware.PostAndPutRequestSizeHistogramMiddleware.Invoke(HttpContext context)
   at App.Metrics.AspNetCore.Tracking.Middleware.ErrorRequestMeterMiddleware.Invoke(HttpContext context)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at App.Metrics.AspNetCore.Tracking.Middleware.ErrorRequestMeterMiddleware.Invoke(HttpContext context)
   at App.Metrics.AspNetCore.Tracking.Middleware.ActiveRequestCounterEndpointMiddleware.Invoke(HttpContext context)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at App.Metrics.AspNetCore.Tracking.Middleware.ActiveRequestCounterEndpointMiddleware.Invoke(HttpContext context)
   at Microsoft.AspNetCore.HostFiltering.HostFilteringMiddleware.Invoke(HttpContext context)
   at NewRelic.Providers.Wrapper.AspNetCore.WrapPipelineMiddleware.Invoke(HttpContext context)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at NewRelic.Providers.Wrapper.AspNetCore.WrapPipelineMiddleware.Invoke(HttpContext context)
   at Microsoft.AspNetCore.Server.IIS.Core.IISHttpContextOfT`1.ProcessRequestAsync()
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at Microsoft.AspNetCore.Server.IIS.Core.IISHttpContextOfT`1.ProcessRequestAsync()
   at Microsoft.AspNetCore.Server.IIS.Core.IISHttpContext.HandleRequest()
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at Microsoft.AspNetCore.Server.IIS.Core.IISHttpContext.HandleRequest()
   at Microsoft.AspNetCore.Server.IIS.Core.IISHttpContext.Execute()
   at System.Threading.ThreadPoolWorkQueue.Dispatch()
   at System.Threading.PortableThreadPool.WorkerThread.WorkerThreadStart()
	None	None	None	{"GUID":"07cca033-1674-4657-8d72-98eec3cfbf4d","IsProtected":false,"ApplicationName":"TrackIT.Web","Category":null,"MachineName":"WIN-U29L07RA6MG","Type":"System.InvalidProgramException","Source":"Serenity.Net.Entity","Message":"TrackIT.GSE.Columns.AssetTripsColumns has a [BasedOnRow(typeof(TrackIT.GSE.Entities.AssetTripsRow), CheckNames = true)] attribute but its 'Operator' property doesn't have a matching field with same property / field name in the row.\n\nPlease check if property is named correctly.\n\nTo remove this validation you may set CheckNames to false on [BasedOnRow] attribute.\n\nTo disable check for this specific property add a [IgnoreName] attribute to the property itself.","Detail":"System.InvalidProgramException: TrackIT.GSE.Columns.AssetTripsColumns has a [BasedOnRow(typeof(TrackIT.GSE.Entities.AssetTripsRow), CheckNames = true)] attribute but its 'Operator' property doesn't have a matching field with same property / field name in the row.\n\nPlease check if property is named correctly.\n\nTo remove this validation you may set CheckNames to false on [BasedOnRow] attribute.\n\nTo disable check for this specific property add a [IgnoreName] attribute to the property itself.\r\n   at Serenity.PropertyGrid.DefaultPropertyItemProvider.GetPropertyItemsFor(Type type) in C:\\Sandbox\\StartSharp\\Serenity\\src\\Serenity.Net.Entity\\PropertyGrid\\DefaultPropertyItemProvider.cs:line 78\r\n   at Serenity.Web.PropertyItemsScript.GetScript() in C:\\Sandbox\\StartSharp\\Serenity\\src\\Serenity.Net.Web\\DynamicScript\\PropertyEditor\\PropertyItemsScript.cs:line 55\r\n   at Serenity.Web.ConcatenatedScript.GetScript() in C:\\Sandbox\\StartSharp\\Serenity\\src\\Serenity.Net.Web\\DynamicScript\\DynamicScriptTypes\\ConcatenatedScript.cs:line 33\r\n   at Serenity.Web.DynamicScriptManager.<>c__DisplayClass16_0.<EnsureScriptContent>g__factory|0() in C:\\Sandbox\\StartSharp\\Serenity\\src\\Serenity.Net.Web\\DynamicScript\\DynamicScript\\DynamicScriptManager.cs:line 132\r\n   at Serenity.MemoryCacheExtensions.Get[TItem](IMemoryCache cache, Object cacheKey, TimeSpan expiration, Func`1 loader) in C:\\Sandbox\\StartSharp\\Serenity\\src\\Serenity.Net.Core\\Caching\\MemoryCacheExtensions.cs:line 64\r\n   at Serenity.Web.DynamicScriptManager.<>c__DisplayClass16_0.<EnsureScriptContent>g__getOrCreate|1() in C:\\Sandbox\\StartSharp\\Serenity\\src\\Serenity.Net.Web\\DynamicScript\\DynamicScript\\DynamicScriptManager.cs:line 141\r\n   at Serenity.Web.DynamicScriptManager.EnsureScriptContent(String name, IDynamicScript script) in C:\\Sandbox\\StartSharp\\Serenity\\src\\Serenity.Net.Web\\DynamicScript\\DynamicScript\\DynamicScriptManager.cs:line 136\r\n   at Serenity.Web.DynamicScriptManager.ReadScriptContent(String name) in C:\\Sandbox\\StartSharp\\Serenity\\src\\Serenity.Net.Web\\DynamicScript\\DynamicScript\\DynamicScriptManager.cs:line 199\r\n   at Serenity.Web.Middleware.DynamicScriptMiddleware.ReturnScript(HttpContext context, String scriptKey, String contentType)\r\n   at Microsoft.AspNetCore.Authorization.AuthorizationMiddleware.Invoke(HttpContext context)\r\n   at Microsoft.AspNetCore.Authentication.AuthenticationMiddleware.Invoke(HttpContext context)\r\n   at StackExchange.Exceptional.ExceptionalMiddleware.Invoke(HttpContext context)\n\nFull Trace:\n\n   at StackExchange.Exceptional.ExceptionalMiddleware.Invoke(HttpContext context)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at StackExchange.Exceptional.ExceptionalMiddleware.Invoke(HttpContext context)\r\n   at Microsoft.AspNetCore.HttpsPolicy.HttpsRedirectionMiddleware.Invoke(HttpContext context)\r\n   at Microsoft.AspNetCore.Diagnostics.DeveloperExceptionPageMiddleware.Invoke(HttpContext context)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at Microsoft.AspNetCore.Diagnostics.DeveloperExceptionPageMiddleware.Invoke(HttpContext context)\r\n   at Microsoft.AspNetCore.Localization.RequestLocalizationMiddleware.Invoke(HttpContext context)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at Microsoft.AspNetCore.Localization.RequestLocalizationMiddleware.Invoke(HttpContext context)\r\n   at Microsoft.AspNetCore.StaticFiles.StaticFileMiddleware.Invoke(HttpContext context)\r\n   at Swashbuckle.AspNetCore.SwaggerUI.SwaggerUIMiddleware.Invoke(HttpContext httpContext)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at Swashbuckle.AspNetCore.SwaggerUI.SwaggerUIMiddleware.Invoke(HttpContext httpContext)\r\n   at Swashbuckle.AspNetCore.Swagger.SwaggerMiddleware.Invoke(HttpContext httpContext, ISwaggerProvider swaggerProvider)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at Swashbuckle.AspNetCore.Swagger.SwaggerMiddleware.Invoke(HttpContext httpContext, ISwaggerProvider swaggerProvider)\r\n   at Microsoft.AspNetCore.Cors.Infrastructure.CorsMiddleware.Invoke(HttpContext context, ICorsPolicyProvider corsPolicyProvider)\r\n   at NWebsec.AspNetCore.Middleware.Middleware.MiddlewareBase.Invoke(HttpContext context)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at NWebsec.AspNetCore.Middleware.Middleware.MiddlewareBase.Invoke(HttpContext context)\r\n   at NWebsec.AspNetCore.Middleware.Middleware.MiddlewareBase.Invoke(HttpContext context)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at NWebsec.AspNetCore.Middleware.Middleware.MiddlewareBase.Invoke(HttpContext context)\r\n   at App.Metrics.AspNetCore.Tracking.Middleware.ApdexMiddleware.MeasureTransaction(HttpContext context)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at App.Metrics.AspNetCore.Tracking.Middleware.ApdexMiddleware.MeasureTransaction(HttpContext context)\r\n   at App.Metrics.AspNetCore.Tracking.Middleware.PerRequestTimerMiddleware.TimeTransaction(HttpContext context)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at App.Metrics.AspNetCore.Tracking.Middleware.PerRequestTimerMiddleware.TimeTransaction(HttpContext context)\r\n   at App.Metrics.AspNetCore.Tracking.Middleware.RequestTimerMiddleware.TimeTransaction(HttpContext context)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at App.Metrics.AspNetCore.Tracking.Middleware.RequestTimerMiddleware.TimeTransaction(HttpContext context)\r\n   at App.Metrics.AspNetCore.Tracking.Middleware.PostAndPutRequestSizeHistogramMiddleware.Invoke(HttpContext context)\r\n   at App.Metrics.AspNetCore.Tracking.Middleware.ErrorRequestMeterMiddleware.Invoke(HttpContext context)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at App.Metrics.AspNetCore.Tracking.Middleware.ErrorRequestMeterMiddleware.Invoke(HttpContext context)\r\n   at App.Metrics.AspNetCore.Tracking.Middleware.ActiveRequestCounterEndpointMiddleware.Invoke(HttpContext context)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at App.Metrics.AspNetCore.Tracking.Middleware.ActiveRequestCounterEndpointMiddleware.Invoke(HttpContext context)\r\n   at Microsoft.AspNetCore.HostFiltering.HostFilteringMiddleware.Invoke(HttpContext context)\r\n   at NewRelic.Providers.Wrapper.AspNetCore.WrapPipelineMiddleware.Invoke(HttpContext context)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at NewRelic.Providers.Wrapper.AspNetCore.WrapPipelineMiddleware.Invoke(HttpContext context)\r\n   at Microsoft.AspNetCore.Server.IIS.Core.IISHttpContextOfT`1.ProcessRequestAsync()\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at Microsoft.AspNetCore.Server.IIS.Core.IISHttpContextOfT`1.ProcessRequestAsync()\r\n   at Microsoft.AspNetCore.Server.IIS.Core.IISHttpContext.HandleRequest()\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at Microsoft.AspNetCore.Server.IIS.Core.IISHttpContext.HandleRequest()\r\n   at Microsoft.AspNetCore.Server.IIS.Core.IISHttpContext.Execute()\r\n   at System.Threading.ThreadPoolWorkQueue.Dispatch()\r\n   at System.Threading.PortableThreadPool.WorkerThread.WorkerThreadStart()\r\n","ErrorHash":1831814775,"CreationDate":"2024-04-04T11:08:27.4943147Z","LastLogDate":null,"StatusCode":null,"CustomData":{},"DuplicateCount":1,"Commands":null,"DeletionDate":null,"Host":"entrackx1.trackit.aero","Url":"/DynJS.axd/ColumnsBundle.js","FullUrl":"https://entrackx1.trackit.aero/DynJS.axd/ColumnsBundle.js?v=638478257063519105","HTTPMethod":"GET","IPAddress":"115.112.167.238","ServerVariablesSerializable":[{"Name":"ContentLength","Value":null},{"Name":"ContentType","Value":null},{"Name":"Host","Value":"entrackx1.trackit.aero"},{"Name":"Path","Value":"/DynJS.axd/ColumnsBundle.js"},{"Name":"PathBase","Value":""},{"Name":"Port","Value":null},{"Name":"Protocol","Value":"HTTP/2"},{"Name":"QueryString","Value":"?v=638478257063519105"},{"Name":"Request Method","Value":"GET"},{"Name":"Scheme","Value":"https"},{"Name":"Url","Value":"https://entrackx1.trackit.aero/DynJS.axd/ColumnsBundle.js?v=638478257063519105"}],"QueryStringSerializable":[{"Name":"v","Value":"638478257063519105"}],"FormSerializable":null,"CookiesSerializable":[{"Name":"_ga","Value":"GA1.2.1375968600.1691117177"},{"Name":"SidebarPaneCollapsed","Value":"1"},{"Name":".AspNetCore.Antiforgery.gKQtFVRMrgk","Value":"CfDJ8J8eE0HTk_BKtO-EP7A1FnkhMLAp8lmim9RzToT5AsWZR7Y2ayBwSLj1C8Di5PUHMNUxNm-iyYKqtoI5RiOFPRfGHYG7r4WF2Xx8pTe2aTRtpSq5QfhIzHo3irAPqLUkPd2HVrmMaO8LmSBSRtOiUow"},{"Name":"CSRF-TOKEN","Value":"CfDJ8J8eE0HTk_BKtO-EP7A1FnmdofGVS1AVLx0Zv1PdbSkypGH1DuX3LJ9lIpT9LrubRuxT60l-Mx2RJDQWcGSEs3y07HJoWqe-C7D2LLJMaNmEsBNfMeBhR6Vik1jVQ5lEDZd9zW01RYp4dDxwJS9qpP4"}],"RequestHeadersSerializable":[{"Name":"Accept","Value":"*/*"},{"Name":"Accept-Encoding","Value":"gzip, deflate, br, zstd"},{"Name":"Accept-Language","Value":"en-US,en;q=0.9"},{"Name":"Connection","Value":"close"},{"Name":"Host","Value":"entrackx1.trackit.aero"},{"Name":"User-Agent","Value":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"},{"Name":"sec-ch-ua","Value":"\"Microsoft Edge\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\""},{"Name":"sec-ch-ua-mobile","Value":"?0"},{"Name":"sec-ch-ua-platform","Value":"\"Windows\""},{"Name":"sec-fetch-site","Value":"same-origin"},{"Name":"sec-fetch-mode","Value":"no-cors"},{"Name":"sec-fetch-dest","Value":"script"}]}	1831814775	1
2	2be60dc3-c6d7-44c5-aacc-03567fb36978	TrackIT.Web	WIN-U29L07RA6MG	2024-04-04 11:08:27.493000	System.InvalidProgramException	False	entrackx1.trackit.aero	/DynJS.axd/FormBundle.js	GET	115.112.167.238	Serenity.Net.Entity	TrackIT.GSE.Forms.AssetTripsForm has a [BasedOnRow(typeof(TrackIT.GSE.Entities.AssetTripsRow), CheckNames = true)] attribute but its 'Operator' property doesn't have a matching field with same property / field name in the row.

Please check if property is named correctly.

To remove this validation you may set CheckNames to false on [BasedOnRow] attribute.

To disable check for this specific property add a [IgnoreName] attribute to the property itself.	System.InvalidProgramException: TrackIT.GSE.Forms.AssetTripsForm has a [BasedOnRow(typeof(TrackIT.GSE.Entities.AssetTripsRow), CheckNames = true)] attribute but its 'Operator' property doesn't have a matching field with same property / field name in the row.

Please check if property is named correctly.

To remove this validation you may set CheckNames to false on [BasedOnRow] attribute.

To disable check for this specific property add a [IgnoreName] attribute to the property itself.
   at Serenity.PropertyGrid.DefaultPropertyItemProvider.GetPropertyItemsFor(Type type) in C:\Sandbox\StartSharp\Serenity\src\Serenity.Net.Entity\PropertyGrid\DefaultPropertyItemProvider.cs:line 78
   at Serenity.Web.PropertyItemsScript.GetScript() in C:\Sandbox\StartSharp\Serenity\src\Serenity.Net.Web\DynamicScript\PropertyEditor\PropertyItemsScript.cs:line 55
   at Serenity.Web.ConcatenatedScript.GetScript() in C:\Sandbox\StartSharp\Serenity\src\Serenity.Net.Web\DynamicScript\DynamicScriptTypes\ConcatenatedScript.cs:line 33
   at Serenity.Web.DynamicScriptManager.<>c__DisplayClass16_0.<EnsureScriptContent>g__factory|0() in C:\Sandbox\StartSharp\Serenity\src\Serenity.Net.Web\DynamicScript\DynamicScript\DynamicScriptManager.cs:line 132
   at Serenity.MemoryCacheExtensions.Get[TItem](IMemoryCache cache, Object cacheKey, TimeSpan expiration, Func`1 loader) in C:\Sandbox\StartSharp\Serenity\src\Serenity.Net.Core\Caching\MemoryCacheExtensions.cs:line 64
   at Serenity.Web.DynamicScriptManager.<>c__DisplayClass16_0.<EnsureScriptContent>g__getOrCreate|1() in C:\Sandbox\StartSharp\Serenity\src\Serenity.Net.Web\DynamicScript\DynamicScript\DynamicScriptManager.cs:line 141
   at Serenity.Web.DynamicScriptManager.EnsureScriptContent(String name, IDynamicScript script) in C:\Sandbox\StartSharp\Serenity\src\Serenity.Net.Web\DynamicScript\DynamicScript\DynamicScriptManager.cs:line 136
   at Serenity.Web.DynamicScriptManager.ReadScriptContent(String name) in C:\Sandbox\StartSharp\Serenity\src\Serenity.Net.Web\DynamicScript\DynamicScript\DynamicScriptManager.cs:line 199
   at Serenity.Web.Middleware.DynamicScriptMiddleware.ReturnScript(HttpContext context, String scriptKey, String contentType)
   at Microsoft.AspNetCore.Authorization.AuthorizationMiddleware.Invoke(HttpContext context)
   at Microsoft.AspNetCore.Authentication.AuthenticationMiddleware.Invoke(HttpContext context)
   at StackExchange.Exceptional.ExceptionalMiddleware.Invoke(HttpContext context)

Full Trace:

   at StackExchange.Exceptional.ExceptionalMiddleware.Invoke(HttpContext context)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at StackExchange.Exceptional.ExceptionalMiddleware.Invoke(HttpContext context)
   at Microsoft.AspNetCore.HttpsPolicy.HttpsRedirectionMiddleware.Invoke(HttpContext context)
   at Microsoft.AspNetCore.Diagnostics.DeveloperExceptionPageMiddleware.Invoke(HttpContext context)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at Microsoft.AspNetCore.Diagnostics.DeveloperExceptionPageMiddleware.Invoke(HttpContext context)
   at Microsoft.AspNetCore.Localization.RequestLocalizationMiddleware.Invoke(HttpContext context)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at Microsoft.AspNetCore.Localization.RequestLocalizationMiddleware.Invoke(HttpContext context)
   at Microsoft.AspNetCore.StaticFiles.StaticFileMiddleware.Invoke(HttpContext context)
   at Swashbuckle.AspNetCore.SwaggerUI.SwaggerUIMiddleware.Invoke(HttpContext httpContext)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at Swashbuckle.AspNetCore.SwaggerUI.SwaggerUIMiddleware.Invoke(HttpContext httpContext)
   at Swashbuckle.AspNetCore.Swagger.SwaggerMiddleware.Invoke(HttpContext httpContext, ISwaggerProvider swaggerProvider)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at Swashbuckle.AspNetCore.Swagger.SwaggerMiddleware.Invoke(HttpContext httpContext, ISwaggerProvider swaggerProvider)
   at Microsoft.AspNetCore.Cors.Infrastructure.CorsMiddleware.Invoke(HttpContext context, ICorsPolicyProvider corsPolicyProvider)
   at NWebsec.AspNetCore.Middleware.Middleware.MiddlewareBase.Invoke(HttpContext context)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at NWebsec.AspNetCore.Middleware.Middleware.MiddlewareBase.Invoke(HttpContext context)
   at NWebsec.AspNetCore.Middleware.Middleware.MiddlewareBase.Invoke(HttpContext context)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at NWebsec.AspNetCore.Middleware.Middleware.MiddlewareBase.Invoke(HttpContext context)
   at App.Metrics.AspNetCore.Tracking.Middleware.ApdexMiddleware.MeasureTransaction(HttpContext context)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at App.Metrics.AspNetCore.Tracking.Middleware.ApdexMiddleware.MeasureTransaction(HttpContext context)
   at App.Metrics.AspNetCore.Tracking.Middleware.PerRequestTimerMiddleware.TimeTransaction(HttpContext context)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at App.Metrics.AspNetCore.Tracking.Middleware.PerRequestTimerMiddleware.TimeTransaction(HttpContext context)
   at App.Metrics.AspNetCore.Tracking.Middleware.RequestTimerMiddleware.TimeTransaction(HttpContext context)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at App.Metrics.AspNetCore.Tracking.Middleware.RequestTimerMiddleware.TimeTransaction(HttpContext context)
   at App.Metrics.AspNetCore.Tracking.Middleware.PostAndPutRequestSizeHistogramMiddleware.Invoke(HttpContext context)
   at App.Metrics.AspNetCore.Tracking.Middleware.ErrorRequestMeterMiddleware.Invoke(HttpContext context)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at App.Metrics.AspNetCore.Tracking.Middleware.ErrorRequestMeterMiddleware.Invoke(HttpContext context)
   at App.Metrics.AspNetCore.Tracking.Middleware.ActiveRequestCounterEndpointMiddleware.Invoke(HttpContext context)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at App.Metrics.AspNetCore.Tracking.Middleware.ActiveRequestCounterEndpointMiddleware.Invoke(HttpContext context)
   at Microsoft.AspNetCore.HostFiltering.HostFilteringMiddleware.Invoke(HttpContext context)
   at NewRelic.Providers.Wrapper.AspNetCore.WrapPipelineMiddleware.Invoke(HttpContext context)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at NewRelic.Providers.Wrapper.AspNetCore.WrapPipelineMiddleware.Invoke(HttpContext context)
   at Microsoft.AspNetCore.Server.IIS.Core.IISHttpContextOfT`1.ProcessRequestAsync()
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at Microsoft.AspNetCore.Server.IIS.Core.IISHttpContextOfT`1.ProcessRequestAsync()
   at Microsoft.AspNetCore.Server.IIS.Core.IISHttpContext.HandleRequest()
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at Microsoft.AspNetCore.Server.IIS.Core.IISHttpContext.HandleRequest()
   at Microsoft.AspNetCore.Server.IIS.Core.IISHttpContext.Execute()
   at System.Threading.ThreadPoolWorkQueue.Dispatch()
   at System.Threading.PortableThreadPool.WorkerThread.WorkerThreadStart()
	None	None	None	{"GUID":"2be60dc3-c6d7-44c5-aacc-03567fb36978","IsProtected":false,"ApplicationName":"TrackIT.Web","Category":null,"MachineName":"WIN-U29L07RA6MG","Type":"System.InvalidProgramException","Source":"Serenity.Net.Entity","Message":"TrackIT.GSE.Forms.AssetTripsForm has a [BasedOnRow(typeof(TrackIT.GSE.Entities.AssetTripsRow), CheckNames = true)] attribute but its 'Operator' property doesn't have a matching field with same property / field name in the row.\n\nPlease check if property is named correctly.\n\nTo remove this validation you may set CheckNames to false on [BasedOnRow] attribute.\n\nTo disable check for this specific property add a [IgnoreName] attribute to the property itself.","Detail":"System.InvalidProgramException: TrackIT.GSE.Forms.AssetTripsForm has a [BasedOnRow(typeof(TrackIT.GSE.Entities.AssetTripsRow), CheckNames = true)] attribute but its 'Operator' property doesn't have a matching field with same property / field name in the row.\n\nPlease check if property is named correctly.\n\nTo remove this validation you may set CheckNames to false on [BasedOnRow] attribute.\n\nTo disable check for this specific property add a [IgnoreName] attribute to the property itself.\r\n   at Serenity.PropertyGrid.DefaultPropertyItemProvider.GetPropertyItemsFor(Type type) in C:\\Sandbox\\StartSharp\\Serenity\\src\\Serenity.Net.Entity\\PropertyGrid\\DefaultPropertyItemProvider.cs:line 78\r\n   at Serenity.Web.PropertyItemsScript.GetScript() in C:\\Sandbox\\StartSharp\\Serenity\\src\\Serenity.Net.Web\\DynamicScript\\PropertyEditor\\PropertyItemsScript.cs:line 55\r\n   at Serenity.Web.ConcatenatedScript.GetScript() in C:\\Sandbox\\StartSharp\\Serenity\\src\\Serenity.Net.Web\\DynamicScript\\DynamicScriptTypes\\ConcatenatedScript.cs:line 33\r\n   at Serenity.Web.DynamicScriptManager.<>c__DisplayClass16_0.<EnsureScriptContent>g__factory|0() in C:\\Sandbox\\StartSharp\\Serenity\\src\\Serenity.Net.Web\\DynamicScript\\DynamicScript\\DynamicScriptManager.cs:line 132\r\n   at Serenity.MemoryCacheExtensions.Get[TItem](IMemoryCache cache, Object cacheKey, TimeSpan expiration, Func`1 loader) in C:\\Sandbox\\StartSharp\\Serenity\\src\\Serenity.Net.Core\\Caching\\MemoryCacheExtensions.cs:line 64\r\n   at Serenity.Web.DynamicScriptManager.<>c__DisplayClass16_0.<EnsureScriptContent>g__getOrCreate|1() in C:\\Sandbox\\StartSharp\\Serenity\\src\\Serenity.Net.Web\\DynamicScript\\DynamicScript\\DynamicScriptManager.cs:line 141\r\n   at Serenity.Web.DynamicScriptManager.EnsureScriptContent(String name, IDynamicScript script) in C:\\Sandbox\\StartSharp\\Serenity\\src\\Serenity.Net.Web\\DynamicScript\\DynamicScript\\DynamicScriptManager.cs:line 136\r\n   at Serenity.Web.DynamicScriptManager.ReadScriptContent(String name) in C:\\Sandbox\\StartSharp\\Serenity\\src\\Serenity.Net.Web\\DynamicScript\\DynamicScript\\DynamicScriptManager.cs:line 199\r\n   at Serenity.Web.Middleware.DynamicScriptMiddleware.ReturnScript(HttpContext context, String scriptKey, String contentType)\r\n   at Microsoft.AspNetCore.Authorization.AuthorizationMiddleware.Invoke(HttpContext context)\r\n   at Microsoft.AspNetCore.Authentication.AuthenticationMiddleware.Invoke(HttpContext context)\r\n   at StackExchange.Exceptional.ExceptionalMiddleware.Invoke(HttpContext context)\n\nFull Trace:\n\n   at StackExchange.Exceptional.ExceptionalMiddleware.Invoke(HttpContext context)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at StackExchange.Exceptional.ExceptionalMiddleware.Invoke(HttpContext context)\r\n   at Microsoft.AspNetCore.HttpsPolicy.HttpsRedirectionMiddleware.Invoke(HttpContext context)\r\n   at Microsoft.AspNetCore.Diagnostics.DeveloperExceptionPageMiddleware.Invoke(HttpContext context)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at Microsoft.AspNetCore.Diagnostics.DeveloperExceptionPageMiddleware.Invoke(HttpContext context)\r\n   at Microsoft.AspNetCore.Localization.RequestLocalizationMiddleware.Invoke(HttpContext context)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at Microsoft.AspNetCore.Localization.RequestLocalizationMiddleware.Invoke(HttpContext context)\r\n   at Microsoft.AspNetCore.StaticFiles.StaticFileMiddleware.Invoke(HttpContext context)\r\n   at Swashbuckle.AspNetCore.SwaggerUI.SwaggerUIMiddleware.Invoke(HttpContext httpContext)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at Swashbuckle.AspNetCore.SwaggerUI.SwaggerUIMiddleware.Invoke(HttpContext httpContext)\r\n   at Swashbuckle.AspNetCore.Swagger.SwaggerMiddleware.Invoke(HttpContext httpContext, ISwaggerProvider swaggerProvider)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at Swashbuckle.AspNetCore.Swagger.SwaggerMiddleware.Invoke(HttpContext httpContext, ISwaggerProvider swaggerProvider)\r\n   at Microsoft.AspNetCore.Cors.Infrastructure.CorsMiddleware.Invoke(HttpContext context, ICorsPolicyProvider corsPolicyProvider)\r\n   at NWebsec.AspNetCore.Middleware.Middleware.MiddlewareBase.Invoke(HttpContext context)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at NWebsec.AspNetCore.Middleware.Middleware.MiddlewareBase.Invoke(HttpContext context)\r\n   at NWebsec.AspNetCore.Middleware.Middleware.MiddlewareBase.Invoke(HttpContext context)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at NWebsec.AspNetCore.Middleware.Middleware.MiddlewareBase.Invoke(HttpContext context)\r\n   at App.Metrics.AspNetCore.Tracking.Middleware.ApdexMiddleware.MeasureTransaction(HttpContext context)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at App.Metrics.AspNetCore.Tracking.Middleware.ApdexMiddleware.MeasureTransaction(HttpContext context)\r\n   at App.Metrics.AspNetCore.Tracking.Middleware.PerRequestTimerMiddleware.TimeTransaction(HttpContext context)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at App.Metrics.AspNetCore.Tracking.Middleware.PerRequestTimerMiddleware.TimeTransaction(HttpContext context)\r\n   at App.Metrics.AspNetCore.Tracking.Middleware.RequestTimerMiddleware.TimeTransaction(HttpContext context)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at App.Metrics.AspNetCore.Tracking.Middleware.RequestTimerMiddleware.TimeTransaction(HttpContext context)\r\n   at App.Metrics.AspNetCore.Tracking.Middleware.PostAndPutRequestSizeHistogramMiddleware.Invoke(HttpContext context)\r\n   at App.Metrics.AspNetCore.Tracking.Middleware.ErrorRequestMeterMiddleware.Invoke(HttpContext context)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at App.Metrics.AspNetCore.Tracking.Middleware.ErrorRequestMeterMiddleware.Invoke(HttpContext context)\r\n   at App.Metrics.AspNetCore.Tracking.Middleware.ActiveRequestCounterEndpointMiddleware.Invoke(HttpContext context)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at App.Metrics.AspNetCore.Tracking.Middleware.ActiveRequestCounterEndpointMiddleware.Invoke(HttpContext context)\r\n   at Microsoft.AspNetCore.HostFiltering.HostFilteringMiddleware.Invoke(HttpContext context)\r\n   at NewRelic.Providers.Wrapper.AspNetCore.WrapPipelineMiddleware.Invoke(HttpContext context)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at NewRelic.Providers.Wrapper.AspNetCore.WrapPipelineMiddleware.Invoke(HttpContext context)\r\n   at Microsoft.AspNetCore.Server.IIS.Core.IISHttpContextOfT`1.ProcessRequestAsync()\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at Microsoft.AspNetCore.Server.IIS.Core.IISHttpContextOfT`1.ProcessRequestAsync()\r\n   at Microsoft.AspNetCore.Server.IIS.Core.IISHttpContext.HandleRequest()\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at Microsoft.AspNetCore.Server.IIS.Core.IISHttpContext.HandleRequest()\r\n   at Microsoft.AspNetCore.Server.IIS.Core.IISHttpContext.Execute()\r\n   at System.Threading.ThreadPoolWorkQueue.Dispatch()\r\n   at System.Threading.PortableThreadPool.WorkerThread.WorkerThreadStart()\r\n","ErrorHash":319502483,"CreationDate":"2024-04-04T11:08:27.4940724Z","LastLogDate":null,"StatusCode":null,"CustomData":{},"DuplicateCount":1,"Commands":null,"DeletionDate":null,"Host":"entrackx1.trackit.aero","Url":"/DynJS.axd/FormBundle.js","FullUrl":"https://entrackx1.trackit.aero/DynJS.axd/FormBundle.js?v=638478257063535216","HTTPMethod":"GET","IPAddress":"115.112.167.238","ServerVariablesSerializable":[{"Name":"ContentLength","Value":null},{"Name":"ContentType","Value":null},{"Name":"Host","Value":"entrackx1.trackit.aero"},{"Name":"Path","Value":"/DynJS.axd/FormBundle.js"},{"Name":"PathBase","Value":""},{"Name":"Port","Value":null},{"Name":"Protocol","Value":"HTTP/2"},{"Name":"QueryString","Value":"?v=638478257063535216"},{"Name":"Request Method","Value":"GET"},{"Name":"Scheme","Value":"https"},{"Name":"Url","Value":"https://entrackx1.trackit.aero/DynJS.axd/FormBundle.js?v=638478257063535216"}],"QueryStringSerializable":[{"Name":"v","Value":"638478257063535216"}],"FormSerializable":null,"CookiesSerializable":[{"Name":"_ga","Value":"GA1.2.1375968600.1691117177"},{"Name":"SidebarPaneCollapsed","Value":"1"},{"Name":".AspNetCore.Antiforgery.gKQtFVRMrgk","Value":"CfDJ8J8eE0HTk_BKtO-EP7A1FnkhMLAp8lmim9RzToT5AsWZR7Y2ayBwSLj1C8Di5PUHMNUxNm-iyYKqtoI5RiOFPRfGHYG7r4WF2Xx8pTe2aTRtpSq5QfhIzHo3irAPqLUkPd2HVrmMaO8LmSBSRtOiUow"},{"Name":"CSRF-TOKEN","Value":"CfDJ8J8eE0HTk_BKtO-EP7A1FnmdofGVS1AVLx0Zv1PdbSkypGH1DuX3LJ9lIpT9LrubRuxT60l-Mx2RJDQWcGSEs3y07HJoWqe-C7D2LLJMaNmEsBNfMeBhR6Vik1jVQ5lEDZd9zW01RYp4dDxwJS9qpP4"}],"RequestHeadersSerializable":[{"Name":"Accept","Value":"*/*"},{"Name":"Accept-Encoding","Value":"gzip, deflate, br, zstd"},{"Name":"Accept-Language","Value":"en-US,en;q=0.9"},{"Name":"Connection","Value":"close"},{"Name":"Host","Value":"entrackx1.trackit.aero"},{"Name":"User-Agent","Value":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"},{"Name":"sec-ch-ua","Value":"\"Microsoft Edge\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\""},{"Name":"sec-ch-ua-mobile","Value":"?0"},{"Name":"sec-ch-ua-platform","Value":"\"Windows\""},{"Name":"sec-fetch-site","Value":"same-origin"},{"Name":"sec-fetch-mode","Value":"no-cors"},{"Name":"sec-fetch-dest","Value":"script"}]}	319502483	1
3	b8f1dd49-0bb9-4ee0-9a80-ee9203f7ddbb	TrackIT.Web	WIN-K15PNSQFLUC	2024-04-04 21:27:04.997000	System.InvalidProgramException	False	192.154.224.158:8018	/DynJS.axd/FormBundle.js	GET	111.7.100.32	Serenity.Net.Entity	TrackIT.Tickets.Forms.AttachmentsForm has a [BasedOnRow(typeof(TrackIT.Tickets.Entities.AttachmentsRow), CheckNames = true)] attribute but its 'TicketId' property doesn't have a matching field with same property / field name in the row.

Please check if property is named correctly.

To remove this validation you may set CheckNames to false on [BasedOnRow] attribute.

To disable check for this specific property add a [IgnoreName] attribute to the property itself.	System.InvalidProgramException: TrackIT.Tickets.Forms.AttachmentsForm has a [BasedOnRow(typeof(TrackIT.Tickets.Entities.AttachmentsRow), CheckNames = true)] attribute but its 'TicketId' property doesn't have a matching field with same property / field name in the row.

Please check if property is named correctly.

To remove this validation you may set CheckNames to false on [BasedOnRow] attribute.

To disable check for this specific property add a [IgnoreName] attribute to the property itself.
   at Serenity.PropertyGrid.DefaultPropertyItemProvider.GetPropertyItemsFor(Type type) in C:\Sandbox\StartSharp\Serenity\src\Serenity.Net.Entity\PropertyGrid\DefaultPropertyItemProvider.cs:line 78
   at Serenity.Web.PropertyItemsScript.GetScript() in C:\Sandbox\StartSharp\Serenity\src\Serenity.Net.Web\DynamicScript\PropertyEditor\PropertyItemsScript.cs:line 55
   at Serenity.Web.ConcatenatedScript.GetScript() in C:\Sandbox\StartSharp\Serenity\src\Serenity.Net.Web\DynamicScript\DynamicScriptTypes\ConcatenatedScript.cs:line 33
   at Serenity.Web.DynamicScriptManager.<>c__DisplayClass16_0.<EnsureScriptContent>g__factory|0() in C:\Sandbox\StartSharp\Serenity\src\Serenity.Net.Web\DynamicScript\DynamicScript\DynamicScriptManager.cs:line 132
   at Serenity.MemoryCacheExtensions.Get[TItem](IMemoryCache cache, Object cacheKey, TimeSpan expiration, Func`1 loader) in C:\Sandbox\StartSharp\Serenity\src\Serenity.Net.Core\Caching\MemoryCacheExtensions.cs:line 50
   at Serenity.Web.DynamicScriptManager.<>c__DisplayClass16_0.<EnsureScriptContent>g__getOrCreate|1() in C:\Sandbox\StartSharp\Serenity\src\Serenity.Net.Web\DynamicScript\DynamicScript\DynamicScriptManager.cs:line 141
   at Serenity.Web.DynamicScriptManager.EnsureScriptContent(String name, IDynamicScript script) in C:\Sandbox\StartSharp\Serenity\src\Serenity.Net.Web\DynamicScript\DynamicScript\DynamicScriptManager.cs:line 146
   at Serenity.Web.DynamicScriptManager.ReadScriptContent(String name) in C:\Sandbox\StartSharp\Serenity\src\Serenity.Net.Web\DynamicScript\DynamicScript\DynamicScriptManager.cs:line 199
   at Serenity.Web.Middleware.DynamicScriptMiddleware.ReturnScript(HttpContext context, String scriptKey, String contentType) in C:\Sandbox\StartSharp\Serenity\src\Serenity.Net.Web\DynamicScript\DynamicScript\DynamicScriptMiddleware.cs:line 48
   at Elastic.Apm.AspNetCore.ApmMiddleware.InvokeAsync(HttpContext context)
   at Microsoft.AspNetCore.Authorization.AuthorizationMiddleware.Invoke(HttpContext context)
   at Microsoft.AspNetCore.Authentication.AuthenticationMiddleware.Invoke(HttpContext context)
   at StackExchange.Exceptional.ExceptionalMiddleware.Invoke(HttpContext context)

Full Trace:

   at StackExchange.Exceptional.ExceptionalMiddleware.Invoke(HttpContext context)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at StackExchange.Exceptional.ExceptionalMiddleware.Invoke(HttpContext context)
   at Microsoft.AspNetCore.HttpsPolicy.HttpsRedirectionMiddleware.Invoke(HttpContext context)
   at Microsoft.AspNetCore.Diagnostics.DeveloperExceptionPageMiddleware.Invoke(HttpContext context)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at Microsoft.AspNetCore.Diagnostics.DeveloperExceptionPageMiddleware.Invoke(HttpContext context)
   at Microsoft.AspNetCore.Localization.RequestLocalizationMiddleware.Invoke(HttpContext context)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at Microsoft.AspNetCore.Localization.RequestLocalizationMiddleware.Invoke(HttpContext context)
   at Microsoft.AspNetCore.StaticFiles.StaticFileMiddleware.Invoke(HttpContext context)
   at Swashbuckle.AspNetCore.SwaggerUI.SwaggerUIMiddleware.Invoke(HttpContext httpContext)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at Swashbuckle.AspNetCore.SwaggerUI.SwaggerUIMiddleware.Invoke(HttpContext httpContext)
   at Swashbuckle.AspNetCore.Swagger.SwaggerMiddleware.Invoke(HttpContext httpContext, ISwaggerProvider swaggerProvider)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at Swashbuckle.AspNetCore.Swagger.SwaggerMiddleware.Invoke(HttpContext httpContext, ISwaggerProvider swaggerProvider)
   at Microsoft.AspNetCore.Builder.UseMiddlewareExtensions.<>c__DisplayClass5_1.<UseMiddleware>b__2(HttpContext context)
   at Microsoft.AspNetCore.Cors.Infrastructure.CorsMiddleware.Invoke(HttpContext context, ICorsPolicyProvider corsPolicyProvider)
   at Microsoft.AspNetCore.Builder.UseMiddlewareExtensions.<>c__DisplayClass5_1.<UseMiddleware>b__2(HttpContext context)
   at NWebsec.AspNetCore.Middleware.Middleware.MiddlewareBase.Invoke(HttpContext context)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at NWebsec.AspNetCore.Middleware.Middleware.MiddlewareBase.Invoke(HttpContext context)
   at NWebsec.AspNetCore.Middleware.Middleware.MiddlewareBase.Invoke(HttpContext context)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at NWebsec.AspNetCore.Middleware.Middleware.MiddlewareBase.Invoke(HttpContext context)
   at App.Metrics.AspNetCore.Tracking.Middleware.ApdexMiddleware.MeasureTransaction(HttpContext context)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at App.Metrics.AspNetCore.Tracking.Middleware.ApdexMiddleware.MeasureTransaction(HttpContext context)
   at App.Metrics.AspNetCore.Tracking.Middleware.ApdexMiddleware.Invoke(HttpContext context)
   at App.Metrics.AspNetCore.Tracking.Middleware.PerRequestTimerMiddleware.TimeTransaction(HttpContext context)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at App.Metrics.AspNetCore.Tracking.Middleware.PerRequestTimerMiddleware.TimeTransaction(HttpContext context)
   at App.Metrics.AspNetCore.Tracking.Middleware.PerRequestTimerMiddleware.Invoke(HttpContext context)
   at App.Metrics.AspNetCore.Tracking.Middleware.RequestTimerMiddleware.TimeTransaction(HttpContext context)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at App.Metrics.AspNetCore.Tracking.Middleware.RequestTimerMiddleware.TimeTransaction(HttpContext context)
   at App.Metrics.AspNetCore.Tracking.Middleware.RequestTimerMiddleware.Invoke(HttpContext context)
   at App.Metrics.AspNetCore.Tracking.Middleware.PostAndPutRequestSizeHistogramMiddleware.Invoke(HttpContext context)
   at App.Metrics.AspNetCore.Tracking.Middleware.ErrorRequestMeterMiddleware.Invoke(HttpContext context)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at App.Metrics.AspNetCore.Tracking.Middleware.ErrorRequestMeterMiddleware.Invoke(HttpContext context)
   at App.Metrics.AspNetCore.Tracking.Middleware.ActiveRequestCounterEndpointMiddleware.Invoke(HttpContext context)
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at App.Metrics.AspNetCore.Tracking.Middleware.ActiveRequestCounterEndpointMiddleware.Invoke(HttpContext context)
   at Microsoft.AspNetCore.HostFiltering.HostFilteringMiddleware.Invoke(HttpContext context)
   at Microsoft.AspNetCore.Hosting.HostingApplication.ProcessRequestAsync(Context context)
   at Microsoft.AspNetCore.Server.IIS.Core.IISHttpContextOfT`1.ProcessRequestAsync()
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at Microsoft.AspNetCore.Server.IIS.Core.IISHttpContextOfT`1.ProcessRequestAsync()
   at Microsoft.AspNetCore.Server.IIS.Core.IISHttpContext.HandleRequest()
   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)
   at Microsoft.AspNetCore.Server.IIS.Core.IISHttpContext.HandleRequest()
   at Microsoft.AspNetCore.Server.IIS.Core.IISHttpContext.Execute()
   at System.Threading.ThreadPoolWorkQueue.Dispatch()
   at System.Threading.PortableThreadPool.WorkerThread.WorkerThreadStart()
   at System.Threading.Thread.StartCallback()
	None	None	None	{"GUID":"b8f1dd49-0bb9-4ee0-9a80-ee9203f7ddbb","IsProtected":false,"ApplicationName":"TrackIT.Web","Category":null,"MachineName":"WIN-K15PNSQFLUC","Type":"System.InvalidProgramException","Source":"Serenity.Net.Entity","Message":"TrackIT.Tickets.Forms.AttachmentsForm has a [BasedOnRow(typeof(TrackIT.Tickets.Entities.AttachmentsRow), CheckNames = true)] attribute but its 'TicketId' property doesn't have a matching field with same property / field name in the row.\n\nPlease check if property is named correctly.\n\nTo remove this validation you may set CheckNames to false on [BasedOnRow] attribute.\n\nTo disable check for this specific property add a [IgnoreName] attribute to the property itself.","Detail":"System.InvalidProgramException: TrackIT.Tickets.Forms.AttachmentsForm has a [BasedOnRow(typeof(TrackIT.Tickets.Entities.AttachmentsRow), CheckNames = true)] attribute but its 'TicketId' property doesn't have a matching field with same property / field name in the row.\n\nPlease check if property is named correctly.\n\nTo remove this validation you may set CheckNames to false on [BasedOnRow] attribute.\n\nTo disable check for this specific property add a [IgnoreName] attribute to the property itself.\r\n   at Serenity.PropertyGrid.DefaultPropertyItemProvider.GetPropertyItemsFor(Type type) in C:\\Sandbox\\StartSharp\\Serenity\\src\\Serenity.Net.Entity\\PropertyGrid\\DefaultPropertyItemProvider.cs:line 78\r\n   at Serenity.Web.PropertyItemsScript.GetScript() in C:\\Sandbox\\StartSharp\\Serenity\\src\\Serenity.Net.Web\\DynamicScript\\PropertyEditor\\PropertyItemsScript.cs:line 55\r\n   at Serenity.Web.ConcatenatedScript.GetScript() in C:\\Sandbox\\StartSharp\\Serenity\\src\\Serenity.Net.Web\\DynamicScript\\DynamicScriptTypes\\ConcatenatedScript.cs:line 33\r\n   at Serenity.Web.DynamicScriptManager.<>c__DisplayClass16_0.<EnsureScriptContent>g__factory|0() in C:\\Sandbox\\StartSharp\\Serenity\\src\\Serenity.Net.Web\\DynamicScript\\DynamicScript\\DynamicScriptManager.cs:line 132\r\n   at Serenity.MemoryCacheExtensions.Get[TItem](IMemoryCache cache, Object cacheKey, TimeSpan expiration, Func`1 loader) in C:\\Sandbox\\StartSharp\\Serenity\\src\\Serenity.Net.Core\\Caching\\MemoryCacheExtensions.cs:line 50\r\n   at Serenity.Web.DynamicScriptManager.<>c__DisplayClass16_0.<EnsureScriptContent>g__getOrCreate|1() in C:\\Sandbox\\StartSharp\\Serenity\\src\\Serenity.Net.Web\\DynamicScript\\DynamicScript\\DynamicScriptManager.cs:line 141\r\n   at Serenity.Web.DynamicScriptManager.EnsureScriptContent(String name, IDynamicScript script) in C:\\Sandbox\\StartSharp\\Serenity\\src\\Serenity.Net.Web\\DynamicScript\\DynamicScript\\DynamicScriptManager.cs:line 146\r\n   at Serenity.Web.DynamicScriptManager.ReadScriptContent(String name) in C:\\Sandbox\\StartSharp\\Serenity\\src\\Serenity.Net.Web\\DynamicScript\\DynamicScript\\DynamicScriptManager.cs:line 199\r\n   at Serenity.Web.Middleware.DynamicScriptMiddleware.ReturnScript(HttpContext context, String scriptKey, String contentType) in C:\\Sandbox\\StartSharp\\Serenity\\src\\Serenity.Net.Web\\DynamicScript\\DynamicScript\\DynamicScriptMiddleware.cs:line 48\r\n   at Elastic.Apm.AspNetCore.ApmMiddleware.InvokeAsync(HttpContext context)\r\n   at Microsoft.AspNetCore.Authorization.AuthorizationMiddleware.Invoke(HttpContext context)\r\n   at Microsoft.AspNetCore.Authentication.AuthenticationMiddleware.Invoke(HttpContext context)\r\n   at StackExchange.Exceptional.ExceptionalMiddleware.Invoke(HttpContext context)\n\nFull Trace:\n\n   at StackExchange.Exceptional.ExceptionalMiddleware.Invoke(HttpContext context)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at StackExchange.Exceptional.ExceptionalMiddleware.Invoke(HttpContext context)\r\n   at Microsoft.AspNetCore.HttpsPolicy.HttpsRedirectionMiddleware.Invoke(HttpContext context)\r\n   at Microsoft.AspNetCore.Diagnostics.DeveloperExceptionPageMiddleware.Invoke(HttpContext context)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at Microsoft.AspNetCore.Diagnostics.DeveloperExceptionPageMiddleware.Invoke(HttpContext context)\r\n   at Microsoft.AspNetCore.Localization.RequestLocalizationMiddleware.Invoke(HttpContext context)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at Microsoft.AspNetCore.Localization.RequestLocalizationMiddleware.Invoke(HttpContext context)\r\n   at Microsoft.AspNetCore.StaticFiles.StaticFileMiddleware.Invoke(HttpContext context)\r\n   at Swashbuckle.AspNetCore.SwaggerUI.SwaggerUIMiddleware.Invoke(HttpContext httpContext)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at Swashbuckle.AspNetCore.SwaggerUI.SwaggerUIMiddleware.Invoke(HttpContext httpContext)\r\n   at Swashbuckle.AspNetCore.Swagger.SwaggerMiddleware.Invoke(HttpContext httpContext, ISwaggerProvider swaggerProvider)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at Swashbuckle.AspNetCore.Swagger.SwaggerMiddleware.Invoke(HttpContext httpContext, ISwaggerProvider swaggerProvider)\r\n   at Microsoft.AspNetCore.Builder.UseMiddlewareExtensions.<>c__DisplayClass5_1.<UseMiddleware>b__2(HttpContext context)\r\n   at Microsoft.AspNetCore.Cors.Infrastructure.CorsMiddleware.Invoke(HttpContext context, ICorsPolicyProvider corsPolicyProvider)\r\n   at Microsoft.AspNetCore.Builder.UseMiddlewareExtensions.<>c__DisplayClass5_1.<UseMiddleware>b__2(HttpContext context)\r\n   at NWebsec.AspNetCore.Middleware.Middleware.MiddlewareBase.Invoke(HttpContext context)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at NWebsec.AspNetCore.Middleware.Middleware.MiddlewareBase.Invoke(HttpContext context)\r\n   at NWebsec.AspNetCore.Middleware.Middleware.MiddlewareBase.Invoke(HttpContext context)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at NWebsec.AspNetCore.Middleware.Middleware.MiddlewareBase.Invoke(HttpContext context)\r\n   at App.Metrics.AspNetCore.Tracking.Middleware.ApdexMiddleware.MeasureTransaction(HttpContext context)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at App.Metrics.AspNetCore.Tracking.Middleware.ApdexMiddleware.MeasureTransaction(HttpContext context)\r\n   at App.Metrics.AspNetCore.Tracking.Middleware.ApdexMiddleware.Invoke(HttpContext context)\r\n   at App.Metrics.AspNetCore.Tracking.Middleware.PerRequestTimerMiddleware.TimeTransaction(HttpContext context)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at App.Metrics.AspNetCore.Tracking.Middleware.PerRequestTimerMiddleware.TimeTransaction(HttpContext context)\r\n   at App.Metrics.AspNetCore.Tracking.Middleware.PerRequestTimerMiddleware.Invoke(HttpContext context)\r\n   at App.Metrics.AspNetCore.Tracking.Middleware.RequestTimerMiddleware.TimeTransaction(HttpContext context)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at App.Metrics.AspNetCore.Tracking.Middleware.RequestTimerMiddleware.TimeTransaction(HttpContext context)\r\n   at App.Metrics.AspNetCore.Tracking.Middleware.RequestTimerMiddleware.Invoke(HttpContext context)\r\n   at App.Metrics.AspNetCore.Tracking.Middleware.PostAndPutRequestSizeHistogramMiddleware.Invoke(HttpContext context)\r\n   at App.Metrics.AspNetCore.Tracking.Middleware.ErrorRequestMeterMiddleware.Invoke(HttpContext context)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at App.Metrics.AspNetCore.Tracking.Middleware.ErrorRequestMeterMiddleware.Invoke(HttpContext context)\r\n   at App.Metrics.AspNetCore.Tracking.Middleware.ActiveRequestCounterEndpointMiddleware.Invoke(HttpContext context)\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at App.Metrics.AspNetCore.Tracking.Middleware.ActiveRequestCounterEndpointMiddleware.Invoke(HttpContext context)\r\n   at Microsoft.AspNetCore.HostFiltering.HostFilteringMiddleware.Invoke(HttpContext context)\r\n   at Microsoft.AspNetCore.Hosting.HostingApplication.ProcessRequestAsync(Context context)\r\n   at Microsoft.AspNetCore.Server.IIS.Core.IISHttpContextOfT`1.ProcessRequestAsync()\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at Microsoft.AspNetCore.Server.IIS.Core.IISHttpContextOfT`1.ProcessRequestAsync()\r\n   at Microsoft.AspNetCore.Server.IIS.Core.IISHttpContext.HandleRequest()\r\n   at System.Runtime.CompilerServices.AsyncMethodBuilderCore.Start[TStateMachine](TStateMachine& stateMachine)\r\n   at Microsoft.AspNetCore.Server.IIS.Core.IISHttpContext.HandleRequest()\r\n   at Microsoft.AspNetCore.Server.IIS.Core.IISHttpContext.Execute()\r\n   at System.Threading.ThreadPoolWorkQueue.Dispatch()\r\n   at System.Threading.PortableThreadPool.WorkerThread.WorkerThreadStart()\r\n   at System.Threading.Thread.StartCallback()\r\n","ErrorHash":-693342639,"CreationDate":"2024-04-04T21:27:04.9969148Z","LastLogDate":null,"StatusCode":null,"CustomData":{},"DuplicateCount":1,"Commands":null,"DeletionDate":null,"Host":"192.154.224.158:8018","Url":"/DynJS.axd/FormBundle.js","FullUrl":"http://192.154.224.158:8018/DynJS.axd/FormBundle.js?v=638478628233362060","HTTPMethod":"GET","IPAddress":"111.7.100.32","ServerVariablesSerializable":[{"Name":"ContentLength","Value":null},{"Name":"ContentType","Value":null},{"Name":"Host","Value":"192.154.224.158"},{"Name":"Path","Value":"/DynJS.axd/FormBundle.js"},{"Name":"PathBase","Value":""},{"Name":"Port","Value":"8018"},{"Name":"Protocol","Value":"HTTP/1.1"},{"Name":"QueryString","Value":"?v=638478628233362060"},{"Name":"Request Method","Value":"GET"},{"Name":"Scheme","Value":"http"},{"Name":"Url","Value":"http://192.154.224.158:8018/DynJS.axd/FormBundle.js?v=638478628233362060"}],"QueryStringSerializable":[{"Name":"v","Value":"638478628233362060"}],"FormSerializable":null,"CookiesSerializable":[{"Name":".AspNetCore.Antiforgery.U4zR6E18704","Value":"CfDJ8KNxMwz_tE9Cng_mhhUiUaOSl0gM_wfEwIWRHNSDEWRGwMzxOwfNlvqd5FmgWr2gh0kBb5Sj3XE2plf_6e69x-3QMa1u8MikgAHo67ibMod4_siuZ7-e0Om8jZ2By70_zNuYwthUjj20fv-Nm02VOAw"},{"Name":"CSRF-TOKEN","Value":"CfDJ8KNxMwz_tE9Cng_mhhUiUaM3TyCDrNAk25GuWvjoqN43NIv-Wln7PAIONCmpRT8b_STO9e7noiL-D_yP6vBOMgVesrBn6IIZJtwVJsgZYa54IQsExam88SntmpUStqKni_yyM6Taj6qLNSxnLDa52Fk"}],"RequestHeadersSerializable":[{"Name":"Accept","Value":"*/*"},{"Name":"Accept-Encoding","Value":"gzip"},{"Name":"Accept-Language","Value":"en"},{"Name":"Connection","Value":"close"},{"Name":"Host","Value":"192.154.224.158:8018"},{"Name":"User-Agent","Value":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}]}	-693342639	1

```

### TABLE: `dbo.FavoriteMenu`

```sql
CREATE TABLE [dbo].[FavoriteMenu] (
  [Id] INTEGER NOT NULL,
  [Title] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [URL] NVARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [CreatedBy] INTEGER
);
```
Sample Rows:
```text
Id	Title	URL	CreatedBy
35	PutAway	https://entrackx1.trackit.aero/CargoWMS/PutAway	2
40	Location	https://hyd.trackit.aero/Location	31
41	Tableau Group	https://hyd.trackit.aero/TableauGroup#	31

```

### TABLE: `dbo.FileSystem`

```sql
CREATE TABLE [dbo].[FileSystem] (
  [Id] INTEGER NOT NULL,
  [FullPath] NVARCHAR(450) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [Filename] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [Extension] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [Size] INTEGER NOT NULL,
  [IsDirectory] BIT NOT NULL,
  [ParentPath] NVARCHAR(450) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Metadata] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Contents] VARBINARY,
  [CreationTime] DATETIME NOT NULL,
  [LastWriteTime] DATETIME NOT NULL
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `dbo.FlightMaster`

```sql
CREATE TABLE [dbo].[FlightMaster] (
  [FlightId] INTEGER NOT NULL,
  [FlightNumber] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [CarrierId] INTEGER,
  [ETD] DATETIME,
  [ETA] DATETIME,
  [ATD] DATETIME,
  [ATA] DATETIME,
  [AirportFromId] INTEGER,
  [AirportToId] INTEGER,
  [AlternateFlightNumber] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [AircraftTailNumber] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [AircraftTypeId] INTEGER,
  [FlightStatus] INTEGER,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
FlightId	FlightNumber	CarrierId	ETD	ETA	ATD	ATA	AirportFromId	AirportToId	AlternateFlightNumber	AircraftTailNumber	AircraftTypeId	FlightStatus	TenantId
1	SRA501	3	2022-12-07 04:15:00	2022-12-07 06:05:00	2022-12-07 04:15:00	2022-12-07 06:05:00	1	5	SRA501	A6-GNY	1	1	1
4	SRA201	3	2022-12-07 13:00:00	2022-12-07 21:00:00	2022-12-07 13:00:00	2022-12-07 21:00:00	1	4	SRA201	A6-JPY	8	1	1
10	F001	22	2022-12-14 00:05:00	2022-12-15 00:25:00	2022-12-14 00:15:00	2022-12-15 00:30:00	31	2	F3456	235666	8	1	1

```

### TABLE: `dbo.GSEDataV`

```sql
CREATE TABLE [dbo].[GSEDataV] (
  [SNO] FLOAT,
  [IMEINo] NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [AssetNo] NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Tenant] NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS"
);
```
Sample Rows:
```text
SNO	IMEINo	AssetNo	Tenant
1.0	866728060451209	101ACU001	NKC
2.0	866728060449856	114ASU003	NKC
3.0	866728060506663	105AML001	NKC

```

### TABLE: `dbo.GSEType_Mapping`

```sql
CREATE TABLE [dbo].[GSEType_Mapping] (
  [code] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Icon_name] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS"
);
```
Sample Rows:
```text
code	Icon_name
10F	PIN
20F	PIN
5F	PIN

```

### TABLE: `dbo.IssueOrderDetail`

```sql
CREATE TABLE [dbo].[IssueOrderDetail] (
  [DetailId] INTEGER NOT NULL,
  [IssueId] INTEGER,
  [CargoId] INTEGER
);
```
Sample Rows:
```text
DetailId	IssueId	CargoId
1	1	1
2	1	2
3	2	1

```

### TABLE: `dbo.IssueOrderMaster`

```sql
CREATE TABLE [dbo].[IssueOrderMaster] (
  [IssueId] INTEGER NOT NULL,
  [RecieverName] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [DeliveryDockNumber] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ESign] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [VehicleNumber] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Remarks] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
IssueId	RecieverName	DeliveryDockNumber	ESign	VehicleNumber	Remarks	TenantId
1	RN01	1	None	1	test	1
2	RN02	1	None	1	None	1
3	RN01	1	None	1	sa	1

```

### TABLE: `dbo.Languages`

```sql
CREATE TABLE [dbo].[Languages] (
  [Id] INTEGER NOT NULL,
  [LanguageId] NVARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [LanguageName] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
Id	LanguageId	LanguageName	TenantId
1	en-GB	English	1
2	ru	Russian	1
3	es	Spanish	1

```

### TABLE: `dbo.Location`

```sql
CREATE TABLE [dbo].[Location] (
  [LocationId] INTEGER NOT NULL,
  [LocationCode] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [LocationName] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [LocationTypeId] INTEGER,
  [ParentLocationId] INTEGER,
  [TenantId] INTEGER NOT NULL,
  [ChildCount] INTEGER,
  [Depth] INTEGER,
  [AnstPath] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [GeoFence] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [geom] NULL,
  [Priority] INTEGER,
  [GeofenceOpacity] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [geocolor] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [geoborderColor] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [xCoordinate] FLOAT,
  [yCoordinate] FLOAT,
  [OwnerId] INTEGER,
  [TotalArea] FLOAT,
  [Utilization] INTEGER,
  [AssetCount] INTEGER,
  [AreaUseTypeId] INTEGER
);
```
Sample Rows:
```text
LocationId	LocationCode	LocationName	LocationTypeId	ParentLocationId	TenantId	ChildCount	Depth	AnstPath	GeoFence	geom	Priority	GeofenceOpacity	geocolor	geoborderColor	xCoordinate	yCoordinate	OwnerId	TotalArea	Utilization	AssetCount	AreaUseTypeId
3	L2	L2	2	0	1	None	None	None	None	None	None	0.6	None	None	None	None	None	None	0	0	None
4	Test Location L1	Test Location L1	2	0	1	None	None	None	None	None	None	0.4	None	None	None	None	None	None	0	0	None
5	User01	Hyderabad	4	4	1	None	None	None	None	None	None	None	None	None	None	None	None	None	0	0	None

```

### TABLE: `dbo.LocationType`

```sql
CREATE TABLE [dbo].[LocationType] (
  [LocationTypeId] INTEGER NOT NULL,
  [Name] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [Icon] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
LocationTypeId	Name	Icon	TenantId
6	Airport	None	5
7	Country	None	5
8	Region	None	5

```

### TABLE: `dbo.LookupData`

```sql
CREATE TABLE [dbo].[LookupData] (
  [LookupDataId] INTEGER NOT NULL,
  [Code] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Name] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [LookupCode] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ModuleId] INTEGER,
  [TenantId] INTEGER,
  [ParentId] INTEGER,
  [Depth] INTEGER,
  [AnstPath] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [F1Value] NVARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [F2Value] NVARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [F3Value] NVARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [F4Value] NVARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [F5Value] NVARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [F6Value] NVARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [F7Value] NVARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [F8Value] NVARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [F9Value] NVARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [F10Value] NVARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS"
);
```
Sample Rows:
```text
LookupDataId	Code	Name	LookupCode	ModuleId	TenantId	ParentId	Depth	AnstPath	F1Value	F2Value	F3Value	F4Value	F5Value	F6Value	F7Value	F8Value	F9Value	F10Value
2	Code1	Name1	Category	2	1	None	None	None	FN1	LN1	2021-09-17	20	True	MCA	None	None	None	None
3	Code1.1	Name1.1	Category	2	1	2	1	Code1	FN2	LN2	2021-09-02	20	False	None	None	None	None	None
4	Code1.1.1	Name1.1.1	Category	2	1	3	2	Code1/Code1.1	FN3	FL3	2021-09-07	20	True	None	None	None	None	None

```

### TABLE: `dbo.LookupMaster`

```sql
CREATE TABLE [dbo].[LookupMaster] (
  [LookupId] INTEGER NOT NULL,
  [LookupCode] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [ModuleId] INTEGER NOT NULL,
  [TenantId] INTEGER NOT NULL,
  [DisplayName] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [HasParent] BIT,
  [Icon] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [EnabledStatus] BIT NOT NULL,
  [NoOfAttribute] INTEGER,
  [F1Name] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [F1Type] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [F1Size] INTEGER,
  [F1Required] BIT,
  [F2Name] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [F2Type] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [F2Size] INTEGER,
  [F2Required] BIT,
  [F3Name] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [F3Type] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [F3Size] INTEGER,
  [F3Required] BIT,
  [F4Name] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [F4Type] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [F4Size] INTEGER,
  [F4Required] BIT,
  [F5Name] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [F5Type] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [F5Size] INTEGER,
  [F5Required] BIT,
  [F6Name] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [F6Type] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [F6Size] INTEGER,
  [F6Required] BIT,
  [F7Name] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [F7Type] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [F7Size] INTEGER,
  [F7Required] BIT,
  [F8Name] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [F8Type] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [F8Size] INTEGER,
  [F8Required] BIT,
  [F9Name] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [F9Type] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [F9Size] INTEGER,
  [F9Required] BIT,
  [F10Name] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [F10Type] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [F10Size] INTEGER,
  [F10Required] BIT
);
```
Sample Rows:
```text
LookupId	LookupCode	ModuleId	TenantId	DisplayName	HasParent	Icon	EnabledStatus	NoOfAttribute	F1Name	F1Type	F1Size	F1Required	F2Name	F2Type	F2Size	F2Required	F3Name	F3Type	F3Size	F3Required	F4Name	F4Type	F4Size	F4Required	F5Name	F5Type	F5Size	F5Required	F6Name	F6Type	F6Size	F6Required	F7Name	F7Type	F7Size	F7Required	F8Name	F8Type	F8Size	F8Required	F9Name	F9Type	F9Size	F9Required	F10Name	F10Type	F10Size	F10Required
105	Active Status	1	1	Active Status	False	None	True	2	ActiveStatusName	String	200	False	ActiveStatusType	String	200	False	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None
22	Active Status	1	5	Active Status	False	None	False	2	ActiveStatusName	String	200	False	ActiveStatusType	String	200	False	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None
197	Active Status	1	6	Active Status	False	None	True	2	ActiveStatusName	String	200	False	ActiveStatusType	String	200	False	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None

```

### TABLE: `dbo.Mail`

```sql
CREATE TABLE [dbo].[Mail] (
  [MailId] BIGINT NOT NULL,
  [UID] UNIQUEIDENTIFIER NOT NULL,
  [Subject] NVARCHAR(400) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [Body] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [MailFrom] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [MailTo] NVARCHAR(2000) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ReplyTo] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [CC] NVARCHAR(2000) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [BCC] NVARCHAR(2000) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Priority] INTEGER NOT NULL,
  [Status] INTEGER NOT NULL,
  [RetryCount] INTEGER NOT NULL,
  [ErrorMessage] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [LockExpiration] DATETIME NOT NULL,
  [SentDate] DATETIME,
  [InsertUserId] INTEGER,
  [InsertDate] DATETIME NOT NULL
);
```
Sample Rows:
```text
MailId	UID	Subject	Body	MailFrom	MailTo	ReplyTo	CC	BCC	Priority	Status	RetryCount	ErrorMessage	LockExpiration	SentDate	InsertUserId	InsertDate
3	75898594-12c9-4b44-8002-f7d5bd44a582	Reset Your EnTrack Password	<html>
<head>
    <title>Reset your StartSharp1 password</title>
</head>
<body>
    <p>Husain Ragib,</p>

    <p>We received a request to change your password on StartSharp1.</p>

    <p>Click the link below to set a new password:</p>

    <p><a href="http://entrackgse.trackit.aero/Account/ResetPassword?t=9r3Y8yHGtiWBc9HZOsKAaEuqHp7CLobSe%2FzKossVr69YavnYmr6sc6R%2FnJVUD9cWylFtVLoj0eEXUdL1LgWT2w%3D%3D">http://entrackgse.trackit.aero/Account/ResetPassword?t=9r3Y8yHGtiWBc9HZOsKAaEuqHp7CLobSe%2FzKossVr69YavnYmr6sc6R%2FnJVUD9cWylFtVLoj0eEXUdL1LgWT2w%3D%3D</a></p>

    <p>If you don't want to change your password, you can ignore this email.</p>

    Thanks,
    The "StartSharp1" Team
</body>
</html>	no-reply@mysite.com	husain@trackit.aero	None	None	None	2	1	1	None	2019-11-14 13:38:27.660000	2019-11-14 13:33:27.677000	None	2019-11-14 13:33:03.630000

```

### TABLE: `dbo.MapLocation`

```sql
CREATE TABLE [dbo].[MapLocation] (
  [MLId] INTEGER NOT NULL,
  [MapId] INTEGER,
  [LocationId] INTEGER,
  [XCoordinate] FLOAT,
  [YCoordinate] FLOAT,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
MLId	MapId	LocationId	XCoordinate	YCoordinate	TenantId
1	1	3	542.0	539.6875	1
2	1	4	452.0	871.6875	1

```

### TABLE: `dbo.MapManagement`

```sql
CREATE TABLE [dbo].[MapManagement] (
  [MapId] INTEGER NOT NULL,
  [MapName] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [MapImage] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
MapId	MapName	MapImage	TenantId
1	Map01	MapManagement/00000/00000001_ym3a4flre37cw.png	1
2	Map02	MapManagement/00000/00000002_d5b54rm2yo66y.png	1

```

### TABLE: `dbo.MasterBeds`

```sql
CREATE TABLE [dbo].[MasterBeds] (
  [BedID] INTEGER NOT NULL,
  [LocationTypeId] INTEGER,
  [LocationID] INTEGER NOT NULL,
  [BedNumber] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [IsActive] BIT NOT NULL,
  [xAxis] DECIMAL(18, 7),
  [yAxis] DECIMAL(18, 7),
  [IsReserved] INTEGER NOT NULL,
  [ReservedBy] INTEGER,
  [ReservedOn] DATETIME,
  [UnReservedBy] INTEGER,
  [UnReservedOn] DATETIME
);
```
Sample Rows:
```text
BedID	LocationTypeId	LocationID	BedNumber	IsActive	xAxis	yAxis	IsReserved	ReservedBy	ReservedOn	UnReservedBy	UnReservedOn
1	1	166	2B Bed 2201	True	-101.6250000	75.0000000	0	1102	2020-04-03 11:21:20.690000	1102	2020-04-03 11:21:24.270000
2	1	167	2B Bed 2202	True	-95.0000000	75.7187500	0	1253	2020-08-11 12:26:35.917000	1253	2020-08-12 08:13:54.313000
3	1	168	2B Bed 2203	True	-88.4749985	76.7000122	0	1102	2020-05-19 17:27:11.770000	1102	2020-05-19 17:27:23.753000

```

### TABLE: `dbo.MasterBlock`

```sql
CREATE TABLE [dbo].[MasterBlock] (
  [BlockID] INTEGER NOT NULL,
  [BlockName] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [BlockPlanSrcPath] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [IsActive] BIT NOT NULL,
  [BuildingID] INTEGER NOT NULL
);
```
Sample Rows:
```text
BlockID	BlockName	BlockPlanSrcPath	IsActive	BuildingID
1003	Block 001	BlockPlan/00001/00001003_hussfzx3m4xe6.png	True	1
1004	Book 002	BlockPlan/00001/00001004_ucdsfm6mj6ciu.jpg	True	2
1005	Block 003	BlockPlan/00001/00001005_tdbw5rbvdj23u.jpg	True	9

```

### TABLE: `dbo.MasterBuilding`

```sql
CREATE TABLE [dbo].[MasterBuilding] (
  [BuildingID] INTEGER NOT NULL,
  [OrganizationId] INTEGER NOT NULL,
  [BuildingCode] NVARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [BuildingName] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [isActive] BIT NOT NULL
);
```
Sample Rows:
```text
BuildingID	OrganizationId	BuildingCode	BuildingName	isActive
1	2	B001	Building 001	True
2	1	B002	Building 002	True
9	5	B003	Building 003	True

```

### TABLE: `dbo.MasterCity`

```sql
CREATE TABLE [dbo].[MasterCity] (
  [CityId] INTEGER NOT NULL,
  [CountryId] INTEGER,
  [CityName] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL
);
```
Sample Rows:
```text
CityId	CountryId	CityName
1	1	Dubai City
2	1	Abu Dhabi City
3	1	Sharjah City

```

### TABLE: `dbo.MasterCountry`

```sql
CREATE TABLE [dbo].[MasterCountry] (
  [CountryId] INTEGER NOT NULL,
  [CountryName] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Code] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS"
);
```
Sample Rows:
```text
CountryId	CountryName	Code
1	UAE	None
2	India	None
3	Afghanistan	AF

```

### TABLE: `dbo.MasterDepartment`

```sql
CREATE TABLE [dbo].[MasterDepartment] (
  [DepartmentID] INTEGER NOT NULL,
  [OrganizationId] INTEGER,
  [LocationId] INTEGER,
  [DepartmentName] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [IsActive] BIT NOT NULL
);
```
Sample Rows:
```text
DepartmentID	OrganizationId	LocationId	DepartmentName	IsActive
13	1	None	General Surgery	True
14	1	None	MRI	True
15	1	None	Orthopedic	True

```

### TABLE: `dbo.MasterFloor`

```sql
CREATE TABLE [dbo].[MasterFloor] (
  [FloorID] INTEGER NOT NULL,
  [BuildingId] INTEGER NOT NULL,
  [BlockID] INTEGER NOT NULL,
  [FloorName] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [FloorPlanSrcPath] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [IsActive] BIT NOT NULL
);
```
Sample Rows:
```text
FloorID	BuildingId	BlockID	FloorName	FloorPlanSrcPath	IsActive
3	1	1003	Floor 1	f1	True
5	2	1004	Floor 2	FloorPlan/00000/00000005_ajrcdcey5bycw.jpg	True
9	9	1005	Floor 3	FloorPlan/00000/00000009_vip22lbpnvwcc.jpg	True

```

### TABLE: `dbo.MasterLocation`

```sql
CREATE TABLE [dbo].[MasterLocation] (
  [LocationID] INTEGER NOT NULL,
  [FloorID] INTEGER NOT NULL,
  [BlockId] INTEGER NOT NULL,
  [BuildingId] INTEGER NOT NULL,
  [LocationName] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [X] FLOAT NOT NULL,
  [Y] FLOAT NOT NULL,
  [IsActive] BIT NOT NULL
);
```
Sample Rows:
```text
LocationID	FloorID	BlockId	BuildingId	LocationName	X	Y	IsActive
1	3	1003	1	Location 1	500.0	500.0	True
2	5	1004	2	Location 2	600.0	600.0	True
3	9	1005	9	Location 3	700.0	700.0	True

```

### TABLE: `dbo.MasterLocationCategory`

```sql
CREATE TABLE [dbo].[MasterLocationCategory] (
  [MasterLocationCategoryId] INTEGER NOT NULL,
  [MasterLocationCategory] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS"
);
```
Sample Rows:
```text
MasterLocationCategoryId	MasterLocationCategory
1	Ward
2	Operation Theater
3	Reception Area

```

### TABLE: `dbo.MasterLocations`

```sql
CREATE TABLE [dbo].[MasterLocations] (
  [LocationID] INTEGER NOT NULL,
  [LocationCategoryID] INTEGER,
  [LocationCode] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [LocationName] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [LocationTypeID] INTEGER NOT NULL,
  [ParentLocationID] INTEGER,
  [LocationPath] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [LocationFlag] INTEGER,
  [isClean] INTEGER,
  [EastX] DECIMAL(18, 7),
  [EastY] DECIMAL(18, 7),
  [WestX] DECIMAL(18, 7),
  [WestY] DECIMAL(18, 7)
);
```
Sample Rows:
```text
LocationID	LocationCategoryID	LocationCode	LocationName	LocationTypeID	ParentLocationID	LocationPath	LocationFlag	isClean	EastX	EastY	WestX	WestY
58	None	None	Parent Organization	1	None	None	None	1	None	None	None	None
59	None	None	Main Building	2	58	temporary/6a6f1c4ac1e943c986c3065a67ed652a.jpg	None	1	None	None	None	None
60	None	None	Ground Floor	3	59	None	None	1	None	None	None	None

```

### TABLE: `dbo.MasterLocationType`

```sql
CREATE TABLE [dbo].[MasterLocationType] (
  [MasterLocationTypeID] INTEGER NOT NULL,
  [LocationType] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [ParentLocationTypeID] INTEGER,
  [IsActive] BIT
);
```
Sample Rows:
```text
MasterLocationTypeID	LocationType	ParentLocationTypeID	IsActive
1	Main Organization	None	True
2	Building No. 1	None	True
3	Floor No. 1	None	True

```

### TABLE: `dbo.MasterOrganization`

```sql
CREATE TABLE [dbo].[MasterOrganization] (
  [OrganizationId] INTEGER NOT NULL,
  [OrganizationName] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [ContactPerson] NVARCHAR(1000) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ContactNumber] NVARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ContactEmail] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Address] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [CountryId] INTEGER NOT NULL,
  [CityId] INTEGER NOT NULL,
  [PostalCode] NVARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS"
);
```
Sample Rows:
```text
OrganizationId	OrganizationName	ContactPerson	ContactNumber	ContactEmail	Address	CountryId	CityId	PostalCode
1	Org 1	None	None	None	Admin Address	1	1	123456
2	Org 2	None	None	None	Test address	1	2	12345
5	Org 3	None	None	None	None	1	5	None

```

### TABLE: `dbo.Masters`

```sql
CREATE TABLE [dbo].[Masters] (
  [MasterID] INTEGER NOT NULL,
  [ModuleID] INTEGER,
  [MasterName] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [MasterValue] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS"
);
```
Sample Rows:
```text
MasterID	ModuleID	MasterName	MasterValue
1	1	Aircraft Master	AircraftMaster
2	1	Airline Master	AirlineMaster
3	1	Make and Model 	AircraftGSE

```

### TABLE: `dbo.MasterStaff`

```sql
CREATE TABLE [dbo].[MasterStaff] (
  [StaffID] INTEGER NOT NULL,
  [OrganizationId] INTEGER NOT NULL,
  [StaffCategoryID] INTEGER NOT NULL,
  [UserID] INTEGER,
  [StaffCode] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [Prefix] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [FirstName] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [LastName] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [FullName] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [Gender] INTEGER,
  [Degree] NVARCHAR(350) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Designation] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Speciality] NVARCHAR(350) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [NumberOfSurgeries] INTEGER,
  [Experience] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Qualifications] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Contact1] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [Contact2] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Email] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [Address] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [IsActive] BIT NOT NULL,
  [RoleId] INTEGER,
  [ProfileImage] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS"
);
```
Sample Rows:
```text
StaffID	OrganizationId	StaffCategoryID	UserID	StaffCode	Prefix	FirstName	LastName	FullName	Gender	Degree	Designation	Speciality	NumberOfSurgeries	Experience	Qualifications	Contact1	Contact2	Email	Address	IsActive	RoleId	ProfileImage
1035	1	1	1049	Srug001	Dr.	Sukinya	Mehra	Dr. Sukinya Mehra	1	None	None	None	None	None	None	1234567890	None	solutionstrackit@gmail.com	None	True	5	UserImage/00001/00001035_o2pzlkynlh5fe.jpg
1036	1	18	1050	Wainsk002	Mr.	Anish	Nair	Mr. Anish Nair	1	None	None	None	None	None	None	1234567890	None	solutionstrackit@gmail.com	None	True	1	UserImage/00001/00001036_2zqewa6rkoup6.jpeg
1037	1	16	1051	MRI001	None	None	None	MRI	1	None	None	None	None	None	None	1234567890	None	solutionstrackit@gmail.com	None	True	5	None

```

### TABLE: `dbo.MasterStaffCategory`

```sql
CREATE TABLE [dbo].[MasterStaffCategory] (
  [StaffCategoryID] INTEGER NOT NULL,
  [OrganizationId] INTEGER NOT NULL,
  [ParentCategoryID] INTEGER,
  [CategoryName] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [IsActive] BIT NOT NULL
);
```
Sample Rows:
```text
StaffCategoryID	OrganizationId	ParentCategoryID	CategoryName	IsActive
1	1	1	Surgeon	True
3	1	None	Hospital Porter	True
4	1	None	Cleaning Staff	True

```

### TABLE: `dbo.MasterStaffDepartment`

```sql
CREATE TABLE [dbo].[MasterStaffDepartment] (
  [StaffDepartmentID] INTEGER NOT NULL,
  [StaffID] INTEGER NOT NULL,
  [DepartmentID] INTEGER NOT NULL
);
```
Sample Rows:
```text
StaffDepartmentID	StaffID	DepartmentID
1	1035	13
3	1037	14
4	1038	15

```

### TABLE: `dbo.MasterStatus`

```sql
CREATE TABLE [dbo].[MasterStatus] (
  [StatusID] INTEGER NOT NULL,
  [OrganizationId] INTEGER NOT NULL,
  [StatusType] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Status] NVARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [IsActive] BIT
);
```
Sample Rows:
```text
StatusID	OrganizationId	StatusType	Status	IsActive
1	4	Patients	OT Schedule Available	True
2	4	Patients	Patient Registered	True
3	4	Patients	Patient In Ward	True

```

### TABLE: `dbo.MaterialCategory`

```sql
CREATE TABLE [dbo].[MaterialCategory] (
  [MaterialCategoryId] INTEGER NOT NULL,
  [MaterialTypeName] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [IsActive] BIT NOT NULL,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
MaterialCategoryId	MaterialTypeName	IsActive	TenantId
1	Life Vests	True	1
2	Oxygen Cylinders	True	1
5	Fire Extinguisher	True	1

```

### TABLE: `dbo.MaterialMaster`

```sql
CREATE TABLE [dbo].[MaterialMaster] (
  [MaterialMasterId] INTEGER NOT NULL,
  [MaterialNumber] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ShortDescription] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [LongDescription] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [MaterialCategoryId] INTEGER,
  [ControlType] INTEGER,
  [Length] FLOAT,
  [Width] FLOAT,
  [Height] FLOAT,
  [Weight] FLOAT,
  [LenUOM] FLOAT,
  [WtUOM] FLOAT,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
MaterialMasterId	MaterialNumber	ShortDescription	LongDescription	MaterialCategoryId	ControlType	Length	Width	Height	Weight	LenUOM	WtUOM	TenantId
1	LV-TRK-01	LV-TRK-01	Life Vest Track	1	3	None	None	None	None	None	None	1
2	M001	SD1	LD1	5	1	None	None	None	None	None	None	1
6	LV-TRK-02	LV-TRK-02	LV Track	16	1	32.0	3.0	66.0	54.0	88.0	68.0	1

```

### TABLE: `dbo.MaterialStock`

```sql
CREATE TABLE [dbo].[MaterialStock] (
  [MaterialStockId] INTEGER NOT NULL,
  [InventoryNumber] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [MaterialNumber] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Quantity] INTEGER,
  [IncomingReference] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [IncomingDate] DATETIME,
  [IncomingRefType] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [OutgoingReference] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [OutgoingDate] DATETIME,
  [OutgoingRefType] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [SerialNumber] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [BatchNumber] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ExpiryDate] DATETIME,
  [Status] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `dbo.MeetingAgendaRelevant`

```sql
CREATE TABLE [dbo].[MeetingAgendaRelevant] (
  [AgendaRelevantId] INTEGER NOT NULL,
  [AgendaId] INTEGER NOT NULL,
  [ContactId] INTEGER NOT NULL
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `dbo.MeetingAgendas`

```sql
CREATE TABLE [dbo].[MeetingAgendas] (
  [AgendaId] INTEGER NOT NULL,
  [MeetingId] INTEGER NOT NULL,
  [AgendaNumber] INTEGER NOT NULL,
  [Title] NVARCHAR(2000) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [Description] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [AgendaTypeId] INTEGER NOT NULL,
  [RequestedByContactId] INTEGER,
  [Images] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Attachments] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS"
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `dbo.MeetingAgendaTypes`

```sql
CREATE TABLE [dbo].[MeetingAgendaTypes] (
  [AgendaTypeId] INTEGER NOT NULL,
  [Name] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL
);
```
Sample Rows:
```text
AgendaTypeId	Name
1	General

```

### TABLE: `dbo.MeetingAttendees`

```sql
CREATE TABLE [dbo].[MeetingAttendees] (
  [AttendeeId] INTEGER NOT NULL,
  [MeetingId] INTEGER NOT NULL,
  [ContactId] INTEGER NOT NULL,
  [AttendeeType] INTEGER NOT NULL,
  [AttendanceStatus] INTEGER NOT NULL
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `dbo.MeetingDecisionRelevant`

```sql
CREATE TABLE [dbo].[MeetingDecisionRelevant] (
  [DecisionRelevantId] INTEGER NOT NULL,
  [DecisionId] INTEGER NOT NULL,
  [ContactId] INTEGER NOT NULL
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `dbo.MeetingDecisions`

```sql
CREATE TABLE [dbo].[MeetingDecisions] (
  [DecisionId] INTEGER NOT NULL,
  [MeetingId] INTEGER NOT NULL,
  [AgendaId] INTEGER,
  [Description] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [DecisionNumber] INTEGER NOT NULL,
  [ResponsibleContactId] INTEGER,
  [DueDate] DATETIME,
  [ResolutionStatus] INTEGER NOT NULL,
  [Images] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Attachments] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS"
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `dbo.MeetingLocations`

```sql
CREATE TABLE [dbo].[MeetingLocations] (
  [LocationId] INTEGER NOT NULL,
  [Name] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [Address] NVARCHAR(300) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Latitude] DECIMAL(14, 6),
  [Longitude] DECIMAL(14, 6)
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `dbo.Meetings`

```sql
CREATE TABLE [dbo].[Meetings] (
  [MeetingId] INTEGER NOT NULL,
  [MeetingName] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [MeetingNumber] NVARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [MeetingGuid] UNIQUEIDENTIFIER NOT NULL,
  [MeetingTypeId] INTEGER NOT NULL,
  [StartDate] DATETIME NOT NULL,
  [EndDate] DATETIME NOT NULL,
  [LocationId] INTEGER,
  [UnitId] INTEGER,
  [OrganizerContactId] INTEGER,
  [ReporterContactId] INTEGER,
  [InsertUserId] INTEGER NOT NULL,
  [InsertDate] DATETIME NOT NULL,
  [UpdateUserId] INTEGER,
  [UpdateDate] DATETIME
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `dbo.MeetingTypes`

```sql
CREATE TABLE [dbo].[MeetingTypes] (
  [MeetingTypeId] INTEGER NOT NULL,
  [Name] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL
);
```
Sample Rows:
```text
MeetingTypeId	Name
1	General

```

### TABLE: `dbo.Module`

```sql
CREATE TABLE [dbo].[Module] (
  [ModuleId] INTEGER NOT NULL,
  [Name] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL
);
```
Sample Rows:
```text
ModuleId	Name
1	GSE
2	Asset
3	Tool

```

### TABLE: `dbo.NotificationGroup`

```sql
CREATE TABLE [dbo].[NotificationGroup] (
  [NotificationGroupId] INTEGER NOT NULL,
  [GroupName] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [NotifyOnEmail] BIT NOT NULL,
  [NotifyOnWhatsapp] BIT NOT NULL,
  [NotifyOnTelegram] BIT NOT NULL,
  [NotifyOnSMS] BIT NOT NULL,
  [CreatedBy] INTEGER NOT NULL,
  [CreatedOn] DATETIME NOT NULL
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `dbo.NotificationGroupEventTypes`

```sql
CREATE TABLE [dbo].[NotificationGroupEventTypes] (
  [NotificationGroupEventTypeId] INTEGER NOT NULL,
  [NotificationGroupId] INTEGER NOT NULL,
  [EventTypesId] INTEGER NOT NULL
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `dbo.NotificationGroupRoles`

```sql
CREATE TABLE [dbo].[NotificationGroupRoles] (
  [NotificationGroupRoleId] INTEGER NOT NULL,
  [NotificationGroupId] INTEGER NOT NULL,
  [RoleId] INTEGER NOT NULL
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `dbo.NotificationGroupUsers`

```sql
CREATE TABLE [dbo].[NotificationGroupUsers] (
  [NotificationGroupUserId] INTEGER NOT NULL,
  [NotificationGroupId] INTEGER NOT NULL,
  [UserId] INTEGER NOT NULL
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `dbo.Notifications`

```sql
CREATE TABLE [dbo].[Notifications] (
  [NotificationID] INTEGER NOT NULL,
  [FlightID] INTEGER,
  [NotificationType] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ActionDate] DATETIME,
  [DismissReq] BIT NOT NULL
);
```
Sample Rows:
```text
NotificationID	FlightID	NotificationType	ActionDate	DismissReq
12	1	MISSING ONBOARD	2022-12-05 16:19:09.460000	False
13	1	ALL DELIVERED	2022-12-05 16:19:17.490000	False
14	1	ALL ONBOARD	2022-12-06 11:01:35.857000	False

```

### TABLE: `dbo.OTSchedule`

```sql
CREATE TABLE [dbo].[OTSchedule] (
  [OTScheduleID] INTEGER NOT NULL,
  [OrganizationId] INTEGER,
  [OpDate] DATETIME NOT NULL,
  [OTListUniqueCode] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [FileName] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [OperationTheatreID] INTEGER NOT NULL,
  [PatientID] INTEGER NOT NULL,
  [Diagnosis] NVARCHAR(1000) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [TreatmentProcedure] NVARCHAR(1000) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [FromTime] DATETIME NOT NULL,
  [ToTime] DATETIME NOT NULL,
  [PAC] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [Remarks] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [ReceivedDate] DATETIME,
  [RecordLastUpdatedOn] DATETIME NOT NULL,
  [IsRecordModified] INTEGER NOT NULL,
  [IsModificationUpdatedonNAS] INTEGER NOT NULL,
  [StatusID] INTEGER NOT NULL,
  [ActualStartAt] DATETIME,
  [ActualEndAt] DATETIME,
  [IsPatientDischarged] INTEGER NOT NULL,
  [LastModifiedBy] INTEGER,
  [LastModifiedDate] DATETIME,
  [TypeOfAnaesthesia] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [AllStaffDetail] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [DeptComment] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [CreatedOn] DATETIME,
  [CreatedBy] INTEGER
);
```
Sample Rows:
```text
OTScheduleID	OrganizationId	OpDate	OTListUniqueCode	FileName	OperationTheatreID	PatientID	Diagnosis	TreatmentProcedure	FromTime	ToTime	PAC	Remarks	ReceivedDate	RecordLastUpdatedOn	IsRecordModified	IsModificationUpdatedonNAS	StatusID	ActualStartAt	ActualEndAt	IsPatientDischarged	LastModifiedBy	LastModifiedDate	TypeOfAnaesthesia	AllStaffDetail	DeptComment	CreatedOn	CreatedBy
329	4	2020-03-17 08:14:50	OT20200317_081455_0640979	OTSchedule (17032020 [Wainks]).xlsx	199	328	Calculus of gallblader w/o choclecystltls obstruction	Laparoscopic cholecystoctomy Code: 871141, 47562	2020-03-17 08:00:00	2020-03-17 09:00:00	10-03-20 ACCEPTED	09-04-2020 DAMAN AUTH#9429493 CODE:0211-11	2020-03-11 15:57:00	2020-03-17 08:14:55.063000	1	1	18	None	None	0	None	None	GENERAL	Dr. Othman, Dr. Sokiyna Mahmoud Shehadeh Alameer	None	2020-03-17 04:14:55.257000	None
330	4	2020-03-17 08:14:50	OT20200317_081455_1010801	OTSchedule (17032020 [Wainks]).xlsx	199	329	Unspecified hemorrhoids CODE: K64.9	Laser ablation of internal hemorrhoids + exc[s] on of external hemorrhoids	2020-03-17 09:15:00	2020-03-17 10:15:00	10-03-20 ACCEPTED	09-04-2020 ADNIC AUTH#E9238163 CODE:45505,462930,46250	2020-03-15 13:57:00	2020-03-17 08:14:55.100000	1	1	18	None	None	0	None	None	GENERAL	Dr. Othman, Dr. Sokiyna Mahmoud Shehadeh Alameer	None	2020-03-17 04:14:55.273000	None
331	4	2020-03-17 08:14:50	OT20200317_081455_1149375	OTSchedule (17032020 [Wainks]).xlsx	199	330	Chrponic anal flasure CODE: K60.1	Fissurectomy and sphinctrotomy Code: 061501, 46200	2020-03-17 10:30:00	2020-03-17 11:30:00	14-03-20 ACCEPTED Allergy: Sea Food	09-04-2020 THIQA AUTH#E69422204 CODE:061501	2020-03-11 13:57:00	2020-03-17 08:14:55.113000	1	1	18	None	None	0	None	None	GENERAL	Dr. Othman, Dr. Sokiyna Mahmoud Shehadeh Alameer	None	2020-03-17 04:14:55.290000	None

```

### TABLE: `dbo.OTScheduleStaff`

```sql
CREATE TABLE [dbo].[OTScheduleStaff] (
  [OTStaffID] INTEGER NOT NULL,
  [OTScheduleID] INTEGER NOT NULL,
  [StaffID] INTEGER NOT NULL,
  [StaffType] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [IsActive] BIT NOT NULL,
  [StatusID] INTEGER,
  [StatusUpdatedOn] DATETIME,
  [FirstEnterAt] DATETIME,
  [LastExitAt] DATETIME,
  [TotalDurationInMins] INTEGER,
  [AssignedOn] DATETIME,
  [AssignedBy] INTEGER,
  [DisassociatedBy] INTEGER,
  [DisasscoiatedOn] DATETIME
);
```
Sample Rows:
```text
OTStaffID	OTScheduleID	StaffID	StaffType	IsActive	StatusID	StatusUpdatedOn	FirstEnterAt	LastExitAt	TotalDurationInMins	AssignedOn	AssignedBy	DisassociatedBy	DisasscoiatedOn
2733	331	1151	Surgeon	True	2	None	None	None	None	2020-03-17 08:15:27.970000	None	None	None
2734	331	1053	Anaesthetist	True	2	None	None	None	None	2020-03-17 08:15:40.857000	None	None	None
2735	330	1151	Surgeon	True	2	None	None	None	None	2020-03-17 08:15:59.917000	None	None	None

```

### TABLE: `dbo.Owner`

```sql
CREATE TABLE [dbo].[Owner] (
  [OwnerId] INTEGER NOT NULL,
  [OwnerCode] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [OwnerName] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantId] INTEGER NOT NULL,
  [ContactName] NVARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Phone] NVARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Email] NVARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [City] NVARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [State] NVARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Country] NVARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Active] BIT,
  [TelegramUser] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Latitude] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Longitude] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [MapIconColor] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS"
);
```
Sample Rows:
```text
OwnerId	OwnerCode	OwnerName	TenantId	ContactName	Phone	Email	City	State	Country	Active	TelegramUser	Latitude	Longitude	MapIconColor
1	BOM	BOM	1	None	None	None	None	None	None	False	None	None	None	None
2	HYD	HYD	1	None	None	None	None	None	None	False	None	None	None	None
10	BAH	BAH	5	None	None	None	None	None	None	True	None	None	None	None

```

### TABLE: `dbo.OwnerLocationUtilization`

```sql
CREATE TABLE [dbo].[OwnerLocationUtilization] (
  [Id] INTEGER NOT NULL,
  [OnwerId] INTEGER,
  [TStamp] DATETIME,
  [LocationId] INTEGER,
  [CurrentCapacity] FLOAT,
  [UtilizedCapacity] FLOAT,
  [CountOfEqp] INTEGER,
  [TenantId] INTEGER
);
```
Sample Rows:
```text
Id	OnwerId	TStamp	LocationId	CurrentCapacity	UtilizedCapacity	CountOfEqp	TenantId
1	183	2025-08-17 05:00:00	1604	7013.859488248825	15.0	3	48
2	184	2025-08-17 05:00:00	1605	4397.851281642914	0.0	0	48
3	183	2025-08-17 06:00:00	1604	7013.859488248825	15.0	3	48

```

### TABLE: `dbo.PalletMaster`

```sql
CREATE TABLE [dbo].[PalletMaster] (
  [PalletId] INTEGER NOT NULL,
  [RFID] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Status] INTEGER,
  [ServiceDate] DATETIME,
  [PalletTypeId] INTEGER,
  [BinId] INTEGER,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
PalletId	RFID	Status	ServiceDate	PalletTypeId	BinId	TenantId
1	10001	1	2022-01-17 00:00:00	1	1	1
4	10003	2	2022-03-10 00:00:00	4	6	28
5	R123456	1	2001-05-01 00:00:00	5	7	1

```

### TABLE: `dbo.PalletType`

```sql
CREATE TABLE [dbo].[PalletType] (
  [PalletTypeId] INTEGER NOT NULL,
  [Code] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Name] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Dimension] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [LoadCapacity] INTEGER,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
PalletTypeId	Code	Name	Dimension	LoadCapacity	TenantId
1	STD	Standard Wooden Pallet	200x200x20	1000	1
2	PLS	Plastic Euro Pallet	200x200x15	1000	1
4	STD	STD	12*12*12	500	28

```

### TABLE: `dbo.Partner`

```sql
CREATE TABLE [dbo].[Partner] (
  [PartnerId] INTEGER NOT NULL,
  [Code] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Name] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ContactPerson] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Email] NVARCHAR(256) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [PhoneNumber] NVARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Address] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [PartnerType] INTEGER,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
PartnerId	Code	Name	ContactPerson	Email	PhoneNumber	Address	PartnerType	TenantId
1	PC-01	PN-01	None	None	None	None	1	1
2	PC-02	PN-02	None	None	None	None	1	1
3	PC-03	PN-03	None	None	None	None	1	1

```

### TABLE: `dbo.PassengerItinerary`

```sql
CREATE TABLE [dbo].[PassengerItinerary] (
  [PassengerId] INTEGER NOT NULL,
  [ReservationId] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [LegNumber] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [PassengerName] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Gender] NVARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [DOB] DATETIME,
  [Phone] NVARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Email] NVARCHAR(256) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [FlightId] INTEGER,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
PassengerId	ReservationId	LegNumber	PassengerName	Gender	DOB	Phone	Email	FlightId	TenantId
1	601023857	01	MR/VEDANTAM/SANDEEP	M	1990-01-01 00:00:00	055 2344253	sandeep@trackit.aero	1	1
2	601023858	01	MR/RAGIB/HUSAIN	M	1979-01-01 00:00:00	0553156721	husain@trackit.aero	1	1
3	601023859	01	MR/SEKHAR/SOMA	M	1990-01-01 00:00:00	0559883838	and@ks.com	1	1

```

### TABLE: `dbo.PassengerUser`

```sql
CREATE TABLE [dbo].[PassengerUser] (
  [UserId] INTEGER NOT NULL,
  [Username] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [DisplayName] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [Email] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [PasswordHash] NVARCHAR(86) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [PasswordSalt] NVARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [InsertDate] DATETIME NOT NULL,
  [IsActive] SMALLINT NOT NULL,
  [MobilePhoneNumber] NVARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [FBToken] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS"
);
```
Sample Rows:
```text
UserId	Username	DisplayName	Email	PasswordHash	PasswordSalt	InsertDate	IsActive	MobilePhoneNumber	FBToken
4	hbragib@gmail.com	Husain Ragib	hbragib@gmail.com	nLQSSA5VK8qoOr9nJMJdMZkEEzb/MrImCMi00DWoUwnDJKf4VeOVwL2DEkvLmqU0nSA0mwC3lcm9PgNI8H2F0A	6378391402	2022-03-21 11:51:57.853000	1	0553156721	dMro-8XOSdSYjwtA8ReiJN:APA91bH9D0jSQC3bD4yrankm85a1sq4XuIPJgcKogWL33leTYsxkWwKYShEOoY_QMzYbf13KUiy2ui0rfABVrOI90XFaG6KI4rrbrki2VK6S7fi-VqE0AuNUACJEkiyrDlSSm-ytKJXR
5	aali.97@yahoo.com	Ahmed Ali	aali.97@yahoo.com	opIL5ZpRMbakB1wpdONnfNd3jUdqnA/uN4u7Eo79/RkR0ulA51kqUBVyObWFbQffPF/A4dcjKFYdkoxlNEdZnA	6378388739	2022-03-24 15:17:50.727000	1	0553156721	None
8	test@t.com	Test	test@t.com	nFwveNhIvW3eLjH18EH9n0rQKns2XZSA9YhwUBcw4RqSNMloiy/0m5GZa7tl4FADL0JWy2yQwy5L/zextWPhkA	6378376251	2022-03-24 23:48:32.720000	1	5808558	None

```

### TABLE: `dbo.Patients`

```sql
CREATE TABLE [dbo].[Patients] (
  [PatientID] INTEGER NOT NULL,
  [FullName] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [UniqueID] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [ContactNumber] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [NationalityID] INTEGER,
  [DoB] DATETIME NOT NULL,
  [Gender] INTEGER NOT NULL,
  [BMI] FLOAT NOT NULL,
  [StatusID] INTEGER,
  [RegisteredOn] DATETIME NOT NULL,
  [IsActive] BIT NOT NULL,
  [LastModifiedBy] INTEGER,
  [LastModifiedDate] DATETIME,
  [OTScheduleId] INTEGER
);
```
Sample Rows:
```text
PatientID	FullName	UniqueID	ContactNumber	NationalityID	DoB	Gender	BMI	StatusID	RegisteredOn	IsActive	LastModifiedBy	LastModifiedDate	OTScheduleId
328	Meron Kereta	UA13000000274992	0504728809	236	1984-03-18 00:00:00	2	31.18	17	2020-03-17 08:14:50	True	None	None	None
329	Fatima Ali Al Sharafi	UA13000000218595	0504150947	249	1994-03-18 00:00:00	2	28.64	17	2020-03-17 08:14:50	True	1104	2020-03-17 08:15:50.733000	330
330	Wedad Obaid Salem Saeed	UA09000000030769	0565500699	69	1990-03-18 00:00:00	2	22.99	17	2020-03-17 08:14:50	True	1104	2020-03-17 08:15:14.813000	331

```

### TABLE: `dbo.ReaderMaster`

```sql
CREATE TABLE [dbo].[ReaderMaster] (
  [ReaderId] INTEGER NOT NULL,
  [Code] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ReaderType] INTEGER,
  [MacAddress] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [IPAddress] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Port] INTEGER,
  [NumberOfAntenna] INTEGER,
  [LocationId] INTEGER,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
ReaderId	Code	ReaderType	MacAddress	IPAddress	Port	NumberOfAntenna	LocationId	TenantId
1	RC-01	1	00:00:5e:00:53:af	192.158.11.38	90	5	None	1
2	TS002	1	00:00:5e:00:53:af	192.158.1.38	1	1	3	1
15	RC-01	1	00:00:5e:00:53:af	192.158.11.38	90	5	None	5

```

### TABLE: `dbo.RolePermissions`

```sql
CREATE TABLE [dbo].[RolePermissions] (
  [RolePermissionId] BIGINT NOT NULL,
  [RoleId] INTEGER NOT NULL,
  [PermissionKey] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL
);
```
Sample Rows:
```text
RolePermissionId	RoleId	PermissionKey
5	3	Ticket
6	3	TicketAttachment
7	3	TicketHistory

```

### TABLE: `dbo.Roles`

```sql
CREATE TABLE [dbo].[Roles] (
  [RoleId] INTEGER NOT NULL,
  [RoleName] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [RoleKey] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantId] INTEGER NOT NULL,
  [InsertUserId] INTEGER
);
```
Sample Rows:
```text
RoleId	RoleName	RoleKey	TenantId	InsertUserId
1	Administration	None	1	None
2	Technician	None	1	None
3	User	None	1	None

```

### TABLE: `dbo.SavedViews`

```sql
CREATE TABLE [dbo].[SavedViews] (
  [Id] UNIQUEIDENTIFIER NOT NULL,
  [TenantId] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [UserId] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ViewName] NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [TableQuery] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [Columns] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [CreatedAt] DATETIME2,
  [UpdatedAt] DATETIME2,
  [IsDefault] BIT
);
```
Sample Rows:
```text
Id	TenantId	UserId	ViewName	TableQuery	Columns	CreatedAt	UpdatedAt	IsDefault
c75e2b92-d4f4-420e-b2d5-064b6ff6b281	20	None	new	{"sql":"SELECT * FROM gse.vwGSEStatus","timestamp":"2025-10-02T04:02:15.977Z"}	[{"accessorKey":"GSE","header":"GSE#","align":"left","id":"col-0-1759377589556"},{"accessorKey":"GSETypeName","header":"Type Name","align":"left","id":"col-2-1759377589556"},{"accessorKey":"OperatorName","header":"Operator","align":"left","id":"col-3-1759377589556"},{"accessorKey":"AllocatedToFlight","header":"Allocated Flight","align":"left","id":"col-4-1759377589556"},{"accessorKey":"HCT","header":"HCT","align":"center","id":"col-8-1759377589556"},{"accessorKey":"EngineStatus","header":"ENG","align":"center","id":"col-5-1759377589556"},{"accessorKey":"OperatingStatus","header":"OPS","align":"center","id":"col-6-1759377589556"},{"accessorKey":"LOP","header":"LOP","align":"center","id":"col-7-1759377589556"},{"accessorKey":"Battery","header":"BAT","align":"center","id":"col-9-1759377589556"},{"accessorKey":"FuelLevel","header":"Fuel/Battery %","align":"left","id":"col-10-1759377589556"},{"accessorKey":"Acceleration","header":"ACC","align":"center","id":"col-11-1759377589556"},{"accessorKey":"BrakingEvents","header":"BKE","align":"center","id":"col-12-1759377589556"},{"accessorKey":"MV","header":"MV (V)","align":"right","id":"col-13-1759377589556"},{"accessorKey":"BV","header":"BV (V)","align":"right","id":"col-14-1759377589556"},{"accessorKey":"OwnerCode","header":"Owner","align":"left","id":"col-15-1759377589556"},{"accessorKey":"FuelLevel","header":"Fuel/Battery %","align":"left","id":"col-16-1759377589556"},{"accessorKey":"CurrentSpeed","header":"Speed","align":"right","id":"col-17-1759377589556"},{"accessorKey":"Overspeeding","header":"Speeding","align":"center","id":"col-18-1759377589556"},{"accessorKey":"Acceleration","header":"ACC","align":"center","id":"col-19-1759377589556"},{"accessorKey":"BrakingEvents","header":"BKE","align":"center","id":"col-20-1759377589556"},{"accessorKey":"LastSeenTime","header":"Last Seen","align":"left","id":"col-21-1759377589556"},{"accessorKey":"LastSeenLocation","header":"LOC","align":"left","id":"col-22-1759377589556"},{"accessorKey":"NextMaintOn","header":"Next PM","align":"left","id":"col-23-1759377589556"},{"accessorKey":"LastMaintOn","header":"Last PM","align":"left","id":"col-24-1759377589556"},{"accessorKey":"MaintenanceStatus","header":"Maint. Status","align":"left","id":"col-25-1759377589556"},{"accessorKey":"CurrentOdometer","header":"ODO (km)","align":"right","id":"col-26-1759377589556"},{"accessorKey":"CurrentEngineHours","header":"ODO (hr)","align":"right","id":"col-27-1759377589556"},{"accessorKey":"StationCode","header":"Station","align":"left","id":"col-28-1759377589556"},{"accessorKey":"TractionHrs","header":"Traction-Hrs","align":"right","id":"col-29-1759377589556"},{"accessorKey":"HydralicHrs","header":"Hydralic-Hrs","align":"right","id":"col-30-1759377589556"},{"accessorKey":"AVP","header":"AVP","align":"left","id":"col-31-1759377589556"},{"accessorKey":"AVPExpiryDate","header":"AVP Expiry","align":"left","id":"col-32-1759377589556"},{"accessorKey":"BatteryCurr","header":"Battery Current","align":"right","id":"col-33-1759377589556"},{"accessorKey":"BatteryTemp","header":"Battery Temp","align":"right","id":"col-34-1759377589556"},{"accessorKey":"SoH","header":"SoH","align":"right","id":"col-35-1759377589556"}]	2025-10-02 04:02:17.170000	2025-10-02 04:02:17.170000	False
284a37ee-dd61-4c68-8883-14405117837e	20	None	Original View	{"sql":"SELECT * FROM gse.vwGSEStatus","timestamp":"2025-10-02T15:26:05.873Z"}	[{"accessorKey":"GSE","header":"GSE#","align":"left"},{"accessorKey":"GSEType","header":"Type","align":"left"},{"accessorKey":"GSETypeName","header":"Type Name","align":"left"},{"accessorKey":"OperatorName","header":"Operator","align":"left"},{"accessorKey":"AllocatedToFlight","header":"Allocated Flight","align":"left"},{"accessorKey":"EngineStatus","header":"ENG","align":"center"},{"accessorKey":"OperatingStatus","header":"OPS","align":"center"},{"accessorKey":"LOP","header":"LOP","align":"center"},{"accessorKey":"HCT","header":"HCT","align":"center"},{"accessorKey":"Battery","header":"BAT","align":"center"},{"accessorKey":"FuelLevel","header":"Fuel/Battery %","align":"left"},{"accessorKey":"Acceleration","header":"ACC","align":"center"},{"accessorKey":"BrakingEvents","header":"BKE","align":"center"},{"accessorKey":"MV","header":"MV (V)","align":"right"},{"accessorKey":"BV","header":"BV (V)","align":"right"},{"accessorKey":"OwnerCode","header":"Owner","align":"left"},{"accessorKey":"FuelLevel","header":"Fuel/Battery %","align":"left"},{"accessorKey":"CurrentSpeed","header":"Speed","align":"right"},{"accessorKey":"Overspeeding","header":"Speeding","align":"center"},{"accessorKey":"Acceleration","header":"ACC","align":"center"},{"accessorKey":"BrakingEvents","header":"BKE","align":"center"},{"accessorKey":"LastSeenTime","header":"Last Seen","align":"left"},{"accessorKey":"LastSeenLocation","header":"LOC","align":"left"},{"accessorKey":"NextMaintOn","header":"Next PM","align":"left"},{"accessorKey":"LastMaintOn","header":"Last PM","align":"left"},{"accessorKey":"MaintenanceStatus","header":"Maint. Status","align":"left"},{"accessorKey":"CurrentOdometer","header":"ODO (km)","align":"right"},{"accessorKey":"CurrentEngineHours","header":"ODO (hr)","align":"right"},{"accessorKey":"StationCode","header":"Station","align":"left"},{"accessorKey":"TractionHrs","header":"Traction-Hrs","align":"right"},{"accessorKey":"HydralicHrs","header":"Hydralic-Hrs","align":"right"},{"accessorKey":"AVP","header":"AVP","align":"left"},{"accessorKey":"AVPExpiryDate","header":"AVP Expiry","align":"left"},{"accessorKey":"BatteryCurr","header":"Battery Current","align":"right"},{"accessorKey":"BatteryTemp","header":"Battery Temp","align":"right"},{"accessorKey":"SoH","header":"SoH","align":"right"}]	2025-10-02 15:26:06.943333	2025-10-02 15:26:06.943333	False
e74d1fe6-82ca-490b-8e67-866d8607b4f2	20	None	test	{"sql":"SELECT * FROM gse.vwGSEStatus","timestamp":"2025-10-01T06:30:05.990Z"}	[{"accessorKey":"GSE","header":"GSE#","align":"left","id":"col-0-1759300197180"},{"accessorKey":"GSEType","header":"Type","align":"left","id":"col-1-1759300197180"},{"accessorKey":"GSETypeName","header":"Type Name","align":"left","id":"col-2-1759300197180"},{"accessorKey":"OperatorName","header":"Operator","align":"left","id":"col-3-1759300197180"},{"accessorKey":"AllocatedToFlight","header":"Allocated Flight","align":"left","id":"col-4-1759300197180"},{"accessorKey":"OperatingStatus","header":"OPS","align":"center","id":"col-6-1759300197180"},{"accessorKey":"LOP","header":"LOP","align":"center","id":"col-7-1759300197180"},{"accessorKey":"HCT","header":"HCT","align":"center","id":"col-8-1759300197180"},{"accessorKey":"Battery","header":"BAT","align":"center","id":"col-9-1759300197180"},{"accessorKey":"FuelLevel","header":"Fuel/Battery %","align":"left","id":"col-10-1759300197180"},{"accessorKey":"Acceleration","header":"ACC","align":"center","id":"col-11-1759300197180"},{"accessorKey":"BrakingEvents","header":"BKE","align":"center","id":"col-12-1759300197180"},{"accessorKey":"MV","header":"MV (V)","align":"right","id":"col-13-1759300197180"},{"accessorKey":"BV","header":"BV (V)","align":"right","id":"col-14-1759300197180"},{"accessorKey":"OwnerCode","header":"Owner","align":"left","id":"col-15-1759300197180"},{"accessorKey":"FuelLevel","header":"Fuel/Battery %","align":"left","id":"col-16-1759300197180"},{"accessorKey":"CurrentSpeed","header":"Speed","align":"right","id":"col-17-1759300197180"},{"accessorKey":"Overspeeding","header":"Speeding","align":"center","id":"col-18-1759300197180"},{"accessorKey":"Acceleration","header":"ACC","align":"center","id":"col-19-1759300197180"},{"accessorKey":"BrakingEvents","header":"BKE","align":"center","id":"col-20-1759300197180"},{"accessorKey":"LastSeenTime","header":"Last Seen","align":"left","id":"col-21-1759300197180"},{"accessorKey":"LastSeenLocation","header":"LOC","align":"left","id":"col-22-1759300197180"},{"accessorKey":"NextMaintOn","header":"Next PM","align":"left","id":"col-23-1759300197180"},{"accessorKey":"LastMaintOn","header":"Last PM","align":"left","id":"col-24-1759300197180"},{"accessorKey":"MaintenanceStatus","header":"Maint. Status","align":"left","id":"col-25-1759300197180"},{"accessorKey":"CurrentOdometer","header":"ODO (km)","align":"right","id":"col-26-1759300197180"},{"accessorKey":"CurrentEngineHours","header":"ODO (hr)","align":"right","id":"col-27-1759300197180"},{"accessorKey":"StationCode","header":"Station","align":"left","id":"col-28-1759300197180"},{"accessorKey":"TractionHrs","header":"Traction-Hrs","align":"right","id":"col-29-1759300197180"},{"accessorKey":"HydralicHrs","header":"Hydralic-Hrs","align":"right","id":"col-30-1759300197180"},{"accessorKey":"AVP","header":"AVP","align":"left","id":"col-31-1759300197180"},{"accessorKey":"AVPExpiryDate","header":"AVP Expiry","align":"left","id":"col-32-1759300197180"},{"accessorKey":"BatteryCurr","header":"Battery Current","align":"right","id":"col-33-1759300197180"},{"accessorKey":"BatteryTemp","header":"Battery Temp","align":"right","id":"col-34-1759300197180"},{"accessorKey":"SoH","header":"SoH","align":"right","id":"col-35-1759300197180"}]	2025-10-01 06:30:07.706666	2025-10-02 15:26:34.840000	True

```

### TABLE: `dbo.ScanPoint`

```sql
CREATE TABLE [dbo].[ScanPoint] (
  [ScanPointId] INTEGER NOT NULL,
  [ScanPoint] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ScanType] INTEGER,
  [AirportId] INTEGER,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
ScanPointId	ScanPoint	ScanType	AirportId	TenantId
1	RUH-CHKIN	1	1	1
2	RUH-BMK	2	1	1
3	RUH-LDG	3	1	1

```

### TABLE: `dbo.ScanPointDetail`

```sql
CREATE TABLE [dbo].[ScanPointDetail] (
  [Id] INTEGER NOT NULL,
  [UserId] INTEGER,
  [ScanPointId] INTEGER,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
Id	UserId	ScanPointId	TenantId
1	1	22	1
2	1	2	1
3	1	3	1

```

### TABLE: `dbo.StockCount`

```sql
CREATE TABLE [dbo].[StockCount] (
  [StockCountId] INTEGER NOT NULL,
  [ScheduleDate] DATETIME,
  [UserId] INTEGER,
  [Status] NVARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [CreatedOn] DATETIME
);
```
Sample Rows:
```text
StockCountId	ScheduleDate	UserId	Status	CreatedOn
1	2021-10-19 00:00:00	None	Pending	2021-10-19 05:33:16.617000
2	2021-10-20 00:00:00	None	Pending	2021-10-19 05:33:38.993000
3	2021-10-22 00:00:00	5	Pending	2021-10-21 15:45:30.150000

```

### TABLE: `dbo.StockCountAsset`

```sql
CREATE TABLE [dbo].[StockCountAsset] (
  [StockCountAssetId] INTEGER NOT NULL,
  [StockCountId] INTEGER,
  [AssetId] INTEGER,
  [Status] NVARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [CheckedOn] DATETIME,
  [CheckedBy] INTEGER,
  [Note] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS"
);
```
Sample Rows:
```text
StockCountAssetId	StockCountId	AssetId	Status	CheckedOn	CheckedBy	Note
1	1	1	Pending	None	None	None
2	1	3	Pending	None	None	None
3	1	4	Pending	None	None	None

```

### TABLE: `dbo.SystemSettings`

```sql
CREATE TABLE [dbo].[SystemSettings] (
  [Id] INTEGER NOT NULL,
  [SettingName] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [SettingValue] VARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantId] INTEGER
);
```
Sample Rows:
```text
Id	SettingName	SettingValue	TenantId
1	SendToEmail	vijai@trackit.aero,sai@trackit.aero	43
3	STE	vijai@trackit.aero,sai@trackit.aero,atq.rampincharge@aiasl.in,abdul.gaffar@aiasl.in,Sushanto.roy@aiasl.in,tm.atq@aiasl.in	43
5	SendToEmail	hbragib@gmail.com,vijai@trackit.aero,mudar@dahbashitech.com,ramdas.r@o.rentals,raheel.s@o.rentals	45

```

### TABLE: `dbo.TableauGroup`

```sql
CREATE TABLE [dbo].[TableauGroup] (
  [GroupId] INTEGER NOT NULL,
  [Name] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [ParentId] INTEGER,
  [ModuleId] INTEGER NOT NULL
);
```
Sample Rows:
```text
GroupId	Name	ParentId	ModuleId
11	Group 01 Group 01 Group 01 Group 01	None	2
12	Group 01 02	11	2
13	Group 01 02 03	12	2

```

### TABLE: `dbo.TableauReport`

```sql
CREATE TABLE [dbo].[TableauReport] (
  [ReportId] INTEGER NOT NULL,
  [PermissionName] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Name] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [URL] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [Options] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Icon] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [GroupId] INTEGER,
  [ModuleId] INTEGER NOT NULL
);
```
Sample Rows:
```text
ReportId	PermissionName	Name	URL	Options	Icon	GroupId	ModuleId
9	Report03	Report03	MRODB/ModuleRepairsPlanActuals	None	fa fa-apple	13	2
14	Report05	Report05	Superstore/Overview	None	fa fa-automobile	16	3
19	NKC Savings ROI	NKC Savings ROI	NKCSavingsROI&#47;Analysis	None	fa fa-list-alt fa-fw	None	1

```

### TABLE: `dbo.TableauReportTags`

```sql
CREATE TABLE [dbo].[TableauReportTags] (
  [TagId] INTEGER NOT NULL,
  [Name] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [ReportId] INTEGER NOT NULL
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `dbo.TableauReportUserAndRole`

```sql
CREATE TABLE [dbo].[TableauReportUserAndRole] (
  [Id] INTEGER NOT NULL,
  [ReportId] INTEGER NOT NULL,
  [ReferenceId] INTEGER NOT NULL,
  [ReferenceType] NVARCHAR(5) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL
);
```
Sample Rows:
```text
Id	ReportId	ReferenceId	ReferenceType
14	74	15	User
15	54	15	User
17	64	15	User

```

### TABLE: `dbo.TenantModule`

```sql
CREATE TABLE [dbo].[TenantModule] (
  [TenantModuleId] INTEGER NOT NULL,
  [ModuleId] INTEGER NOT NULL,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
TenantModuleId	ModuleId	TenantId
1	1	5
2	3	1
3	2	1

```

### TABLE: `dbo.Tenants`

```sql
CREATE TABLE [dbo].[Tenants] (
  [TenantId] INTEGER NOT NULL,
  [TenantName] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [HQ] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantType] INTEGER,
  [TenantEmail] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantKey] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantLogo] IMAGE
);
```
Sample Rows:
```text
TenantId	TenantName	HQ	TenantType	TenantEmail	TenantKey	TenantLogo
1	TrackITInternal	Surat	None	husain@trackit.aero	VHJhY2tJVEludGVybmFs	None
5	SAL	None	565	husain@trackit.aero	U0FM	None
6	BAH	None	None	husain@trackit.aero	QkFI	None

```

### TABLE: `dbo.TenantSettings`

```sql
CREATE TABLE [dbo].[TenantSettings] (
  [Id] INTEGER NOT NULL,
  [Name] INTEGER NOT NULL,
  [Value] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantID] INTEGER NOT NULL
);
```
Sample Rows:
```text
Id	Name	Value	TenantID
1	1	39.15642	5
2	2	21.671403	5
3	1	50.617644	6

```

### TABLE: `dbo.TicketAttachments`

```sql
CREATE TABLE [dbo].[TicketAttachments] (
  [AttachmentId] INTEGER NOT NULL,
  [FileName] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TicketHistoryId] INTEGER NOT NULL,
  [FileUrl] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [UploadedOn] DATETIME NOT NULL
);
```
Sample Rows:
```text
AttachmentId	FileName	TicketHistoryId	FileUrl	UploadedOn
10	None	18	[{"OriginalName":"2.jpg","Filename":"temporary/02a1b4d04f37407ca9c4a8b8bcd1c0fa.jpg"}]	2021-08-20 16:18:18.687000

```

### TABLE: `dbo.TicketHistory`

```sql
CREATE TABLE [dbo].[TicketHistory] (
  [TicketHistoryId] INTEGER NOT NULL,
  [TicketId] INTEGER NOT NULL,
  [Description] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Reply] BIT,
  [CreatedOn] DATETIME NOT NULL,
  [CreatedBy] INTEGER
);
```
Sample Rows:
```text
TicketHistoryId	TicketId	Description	Reply	CreatedOn	CreatedBy
18	20	by admin	False	2021-08-20 16:18:18.530000	1
20	20	testing answered status	True	2021-08-20 16:47:51.257000	1

```

### TABLE: `dbo.TicketIssueType`

```sql
CREATE TABLE [dbo].[TicketIssueType] (
  [IssueTypeId] INTEGER NOT NULL,
  [Name] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL
);
```
Sample Rows:
```text
IssueTypeId	Name
1	Technical
2	UI
3	Performance

```

### TABLE: `dbo.TicketPriority`

```sql
CREATE TABLE [dbo].[TicketPriority] (
  [PriorityId] INTEGER NOT NULL,
  [Name] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL
);
```
Sample Rows:
```text
PriorityId	Name
1	High
2	Low

```

### TABLE: `dbo.Tickets`

```sql
CREATE TABLE [dbo].[Tickets] (
  [TicketId] INTEGER NOT NULL,
  [Title] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [Description] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [PriorityId] INTEGER NOT NULL,
  [IssueTypeId] INTEGER NOT NULL,
  [ModuleId] INTEGER NOT NULL,
  [Status] NVARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [CreatedOn] DATETIME NOT NULL,
  [ClosedOn] DATETIME,
  [CreatedBy] INTEGER,
  [ClosedBy] INTEGER,
  [TenantId] INTEGER NOT NULL,
  [TicketNumber] NVARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL
);
```
Sample Rows:
```text
TicketId	Title	Description	PriorityId	IssueTypeId	ModuleId	Status	CreatedOn	ClosedOn	CreatedBy	ClosedBy	TenantId	TicketNumber
20	Created By Admin	by admin	1	3	2	Closed	2021-08-20 16:18:18.347000	2021-10-14 12:20:22.010000	1	1	1	TCKN-00007
21	Bug	None	2	3	1	Closed	2021-08-20 17:36:48.077000	2021-10-14 12:19:56.200000	1	1	1	TCKN-00008
26	Mapticket	None	2	2	1	Open	2022-03-31 10:46:21.813000	None	15	None	5	TCKN-00013

```

### TABLE: `dbo.TimeZone`

```sql
CREATE TABLE [dbo].[TimeZone] (
  [id] INTEGER NOT NULL,
  [TimeZoneName] NVARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TimeZoneValue] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS"
);
```
Sample Rows:
```text
id	TimeZoneName	TimeZoneValue
1	International Date Line West (Etc/GMT+12)	-12:00
2	Midway Island, Samoa (Pacific/Midway)	-11:00
3	Hawaii (Pacific/Honolulu)	-10:00

```

### TABLE: `dbo.tmpAccessControl`

```sql
CREATE TABLE [dbo].[tmpAccessControl] (
  [Id] INTEGER NOT NULL,
  [DeviceID] INTEGER,
  [OperatorID] INTEGER,
  [Position] INTEGER,
  [PushDate] DATETIME,
  [Confirmed] DATETIME,
  [IMEI] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [CardID] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS"
);
```
Sample Rows:
```text
Id	DeviceID	OperatorID	Position	PushDate	Confirmed	IMEI	CardID
1	398	9	30000	None	None	None	None
2	398	10	30001	None	None	None	None
3	398	11	30002	None	None	None	None

```

### TABLE: `dbo.tmpCommands`

```sql
CREATE TABLE [dbo].[tmpCommands] (
  [Id] INTEGER NOT NULL,
  [DeviceID] INTEGER,
  [Command] VARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [PushDate] DATETIME,
  [Response] VARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ResponseDate] DATETIME,
  [ExpectedResponse] VARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS"
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `dbo.Tool`

```sql
CREATE TABLE [dbo].[Tool] (
  [ToolId] INTEGER NOT NULL,
  [Description] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [UniqueId] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ToolTypeId] INTEGER,
  [ToolCategoryId] INTEGER,
  [DateOfPurchase] DATETIME,
  [NoOfCycles] INTEGER,
  [RequireCalibration] BIT,
  [Attachment] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [AttachmentDescription] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Status] INTEGER,
  [LastCheckout] DATETIME,
  [CheckoutBy] INTEGER,
  [ReturnExpected] DATETIME,
  [IsCheckout] BIT,
  [IsVendorOwned] BIT,
  [PartnerId] INTEGER,
  [LocationId] INTEGER,
  [IsToolKit] BIT,
  [ToolKitId] INTEGER,
  [Quantity] INTEGER,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
ToolId	Description	UniqueId	ToolTypeId	ToolCategoryId	DateOfPurchase	NoOfCycles	RequireCalibration	Attachment	AttachmentDescription	Status	LastCheckout	CheckoutBy	ReturnExpected	IsCheckout	IsVendorOwned	PartnerId	LocationId	IsToolKit	ToolKitId	Quantity	TenantId
1	Desc01	UID-01	1	1	2021-11-11 00:00:00	0	False	None	None	1	2021-11-20 10:08:04.710000	1	None	False	None	None	None	False	3	20	1
2	Desc 02	UID-02	1	1	2021-11-04 00:00:00	0	False	None	None	1	None	None	None	None	False	None	3	False	3	20	1
3	Tool Kit 01	TK-00001	18	1	2023-09-19 00:00:00	None	False	None	None	None	None	None	None	None	False	None	4	True	None	None	1

```

### TABLE: `dbo.ToolCategory`

```sql
CREATE TABLE [dbo].[ToolCategory] (
  [ToolCategoryId] INTEGER NOT NULL,
  [Code] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Description] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [IsActive] BIT NOT NULL,
  [CanDepreciate] BIT NOT NULL,
  [CanReserve] BIT NOT NULL,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
ToolCategoryId	Code	Description	IsActive	CanDepreciate	CanReserve	TenantId
1	PT	Power Tools	True	False	True	1
2	CT	Construction Tools	True	True	True	1
4	TC-01	Tool Category 01	True	True	True	28

```

### TABLE: `dbo.ToolHistory`

```sql
CREATE TABLE [dbo].[ToolHistory] (
  [ToolHistoryId] INTEGER NOT NULL,
  [ToolId] INTEGER NOT NULL,
  [Type] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Description] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [CreatedOn] DATETIME,
  [CreatedBy] INTEGER
);
```
Sample Rows:
```text
ToolHistoryId	ToolId	Type	Description	CreatedOn	CreatedBy
1	1	Check In / Check Out	Tool Checked Out, checkout by- admin, Return Date - 03 Nov, 2021.	2021-11-20 10:08:04.883000	1
2	1	Check In / Check Out	Tool CheckIn.	2021-11-20 10:22:29.293000	1
3	1	Mark as Damaged	Tool status updated to Damaged.	2021-11-20 14:59:21.243000	1

```

### TABLE: `dbo.ToolMaintainenceSchedule`

```sql
CREATE TABLE [dbo].[ToolMaintainenceSchedule] (
  [TMSId] INTEGER NOT NULL,
  [ScheduleName] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ScheduleType] INTEGER,
  [NoOfDays] INTEGER,
  [NoOfCycles] INTEGER,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
TMSId	ScheduleName	ScheduleType	NoOfDays	NoOfCycles	TenantId
1	SN 01	2	None	20	1
4	SN 02	2	None	3	28
5	c1	1	1	None	1

```

### TABLE: `dbo.ToolReservation`

```sql
CREATE TABLE [dbo].[ToolReservation] (
  [ToolReservationId] INTEGER NOT NULL,
  [ReservationNumber] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ToolId] INTEGER,
  [ReservedFrom] DATETIME,
  [ReservedTo] DATETIME,
  [ReservedOn] DATETIME,
  [ReservedBy] INTEGER,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
ToolReservationId	ReservationNumber	ToolId	ReservedFrom	ReservedTo	ReservedOn	ReservedBy	TenantId
2	TR-00002	2	2021-11-20 16:10:45.353000	2021-11-25 16:10:45.353000	2021-11-25 16:10:45.353000	1	1
4	TR-00004	4	2021-12-01 16:10:45.353000	2021-12-20 16:10:45.353000	2022-01-04 10:58:34.070000	1	1
8	TR-00008	13	2022-12-01 00:00:00	2022-12-20 00:00:00	2022-12-19 01:24:06.890000	1	1

```

### TABLE: `dbo.Toolset`

```sql
CREATE TABLE [dbo].[Toolset] (
  [ToolsetId] INTEGER NOT NULL,
  [Code] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Description] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [CreatedBy] INTEGER,
  [CreatedOn] DATETIME,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
ToolsetId	Code	Description	CreatedBy	CreatedOn	TenantId
1	TS001	TS 001	1	2021-11-25 00:00:00	1
2	TS002	TS-002	1	2022-01-06 15:47:27.090000	1
4	TS1	TSD1	1	2022-10-19 07:37:02.087000	28

```

### TABLE: `dbo.ToolsetDetail`

```sql
CREATE TABLE [dbo].[ToolsetDetail] (
  [ToolsetDetailId] INTEGER NOT NULL,
  [ToolsetId] INTEGER,
  [ToolTypeId] INTEGER,
  [Quantity] INTEGER
);
```
Sample Rows:
```text
ToolsetDetailId	ToolsetId	ToolTypeId	Quantity
2	1	1	2
9	2	5	1
10	17	18	2

```

### TABLE: `dbo.ToolType`

```sql
CREATE TABLE [dbo].[ToolType] (
  [ToolTypeId] INTEGER NOT NULL,
  [Code] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Description] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Manufacturer] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ModelNumber] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TMSId] INTEGER,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
ToolTypeId	Code	Description	Manufacturer	ModelNumber	TMSId	TenantId
1	TTC 01	Descritption 01	M01	MO-01	1	1
4	TTC 02	TS-002	m02	12	4	28
5	c1	n1	tstc1	334566	5	1

```

### TABLE: `dbo.TrolleyMaster`

```sql
CREATE TABLE [dbo].[TrolleyMaster] (
  [TrolleyId] INTEGER NOT NULL,
  [TagId] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [SerialNumber] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TrolleyTypeId] INTEGER,
  [ServiceDate] DATETIME,
  [FirstSeenTime] DATETIME,
  [LastSeenTime] DATETIME,
  [LastSeenLocation] INTEGER,
  [Status] INTEGER,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
TrolleyId	TagId	SerialNumber	TrolleyTypeId	ServiceDate	FirstSeenTime	LastSeenTime	LastSeenLocation	Status	TenantId
1	T-01	SN-893764	1	2022-02-11 00:00:00	2022-02-11 00:00:00	None	None	1	1
2	T-02	SN-893765	1	2022-02-21 00:00:00	2022-02-21 00:00:00	2022-02-21 00:00:00	3	1	1
3	TAG1	123444	3	2022-10-21 00:00:00	None	None	None	1	1

```

### TABLE: `dbo.TrolleyTypeMaster`

```sql
CREATE TABLE [dbo].[TrolleyTypeMaster] (
  [TrolleyTypeId] INTEGER NOT NULL,
  [Code] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Name] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
TrolleyTypeId	Code	Name	TenantId
1	TTC01	TTN01	1
2	TTC01	TTN01	28
3	C1	N1	1

```

### TABLE: `dbo.UserOwner`

```sql
CREATE TABLE [dbo].[UserOwner] (
  [Id] INTEGER NOT NULL,
  [UserId] INTEGER NOT NULL,
  [OwnerId] INTEGER NOT NULL
);
```
Sample Rows:
```text
Id	UserId	OwnerId
2	42	162
4	45	176
6	52	177

```

### TABLE: `dbo.UserPermissions`

```sql
CREATE TABLE [dbo].[UserPermissions] (
  [UserPermissionId] BIGINT NOT NULL,
  [UserId] INTEGER NOT NULL,
  [PermissionKey] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [Granted] BIT NOT NULL
);
```
Sample Rows:
```text
UserPermissionId	UserId	PermissionKey	Granted
18	4	TableauReport: Report01	True
21	4	TableauReport: Report02	True
30	15	MapView:MapPlayBack	True

```

### TABLE: `dbo.UserPreferences`

```sql
CREATE TABLE [dbo].[UserPreferences] (
  [UserPreferenceId] INTEGER NOT NULL,
  [UserId] BIGINT NOT NULL,
  [PreferenceType] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [Name] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [Value] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS"
);
```
Sample Rows:
```text
UserPreferenceId	UserId	PreferenceType	Name	Value
1	44	UserPreferenceStorage	GridSettings::TrackIT.GSE.GSEStatusGrid	{"columns":[{"id":"StationCode","visible":true,"width":117.625,"sort":0},{"id":"Gse","visible":true,"width":133.844,"sort":0},{"id":"LastSeenTime","visible":true,"width":133.5,"sort":-1},{"id":"GseType","visible":true,"width":90.75,"sort":0},{"id":"CurrentEngineHours","visible":true,"width":94.6484,"sort":0},{"id":"EngineStatus","visible":true,"width":42.30769230769231,"sort":0},{"id":"OperatingStatus","visible":true,"width":42.30769230769231,"sort":0},{"id":"Battery","visible":true,"width":42.30769230769231,"sort":0},{"id":"Acceleration","visible":true,"width":42.30769230769231,"sort":0},{"id":"BrakingEvents","visible":true,"width":42.30769230769231,"sort":0},{"id":"CurrentSpeed","visible":true,"width":117.6923076923077,"sort":0},{"id":"MV","visible":true,"width":124.289,"sort":0},{"id":"FuelLevel","visible":true,"width":143.297,"sort":0},{"id":"LastSeenLocation","visible":true,"width":299.215,"sort":0},{"id":"InMaintenanceUnPlan","visible":true,"width":117.656,"sort":0},{"id":"Fuel","visible":true,"width":98.5273,"sort":0},{"id":"MaintCreatedOn","visible":true,"width":101.53846153846153,"sort":0},{"id":"NextMaintOn","visible":true,"width":117.6923076923077,"sort":0},{"id":"MaintenanceType","visible":true,"width":80,"sort":0},{"id":"OperatorName","visible":true,"width":171.53846153846152,"sort":0},{"id":"OwnerCode","visible":true,"width":117.6923076923077,"sort":0},{"id":"CurrentOdometer","visible":true,"width":117.6923076923077,"sort":0}],"includeDeleted":false,"quickFilters":{"GSEID":[],"EquipmentTypeID":"","OwnerId":"","StationId":"11","MaintenanceType":"","LastSeenTime":[null,null],"LastSeenLocation":"","OperatorName":""}}
2	44	UserPreferenceStorage	Views:GridSettings::TrackIT.GSE.GSEStatusGrid	{"Demo":{"columns":[{"id":"Gse","visible":true,"width":85.8167,"sort":0},{"id":"GseType","visible":true,"width":73.7667,"sort":0},{"id":"EngineStatus","visible":true,"width":42.3,"sort":0},{"id":"OperatingStatus","visible":true,"width":42.3,"sort":0},{"id":"Lop","visible":true,"width":42.3,"sort":0},{"id":"Hct","visible":true,"width":42.3,"sort":0},{"id":"Battery","visible":true,"width":42.3,"sort":0},{"id":"Acceleration","visible":true,"width":56.3,"sort":0},{"id":"BrakingEvents","visible":true,"width":42.3,"sort":0},{"id":"FuelLevel","visible":true,"width":86.3,"sort":0},{"id":"MV","visible":true,"width":124.3,"sort":0},{"id":"LastSeenLocation","visible":true,"width":139.217,"sort":0},{"id":"CurrentSpeed","visible":true,"width":117.667,"sort":0},{"id":"NextMaintOn","visible":true,"width":117.667,"sort":0},{"id":"InMaintenanceUnPlan","visible":true,"width":117.667,"sort":0},{"id":"MaintenanceType","visible":true,"width":105,"sort":0},{"id":"MaintCreatedBy","visible":true,"width":171.517,"sort":0},{"id":"MaintCreatedOn","visible":true,"width":101.517,"sort":0},{"id":"ExceptionNotes","visible":true,"width":140.517,"sort":0},{"id":"CurrentEngineHours","visible":true,"width":82.6667,"sort":0},{"id":"CurrentOdometer","visible":true,"width":102.683,"sort":0},{"id":"LastSeenTime","visible":true,"width":135.517,"sort":-1}],"includeDeleted":false,"quickFilters":{"GSEID":"","EquipmentTypeID":"","DriverID":"","OwnerId":"","StationId":"","LastSeenLocationId":"","MaintenanceType":"","LastSeenTime":[null,null]}},"demo":{"columns":[{"id":"Gse","visible":true,"width":85.8167,"sort":0},{"id":"GseType","visible":true,"width":73.7667,"sort":0},{"id":"EngineStatus","visible":true,"width":42.30769230769231,"sort":0},{"id":"OperatingStatus","visible":true,"width":42.30769230769231,"sort":0},{"id":"Lop","visible":true,"width":42.30769230769231,"sort":0},{"id":"Hct","visible":true,"width":42.30769230769231,"sort":0},{"id":"Battery","visible":true,"width":42.30769230769231,"sort":0},{"id":"Acceleration","visible":true,"width":56.3,"sort":0},{"id":"BrakingEvents","visible":true,"width":42.30769230769231,"sort":0},{"id":"FuelLevel","visible":true,"width":86.3,"sort":0},{"id":"MV","visible":true,"width":124.3,"sort":0},{"id":"LastSeenLocation","visible":true,"width":139.217,"sort":0},{"id":"CurrentSpeed","visible":true,"width":117.667,"sort":0},{"id":"NextMaintOn","visible":true,"width":117.667,"sort":0},{"id":"InMaintenanceUnPlan","visible":true,"width":117.667,"sort":0},{"id":"MaintenanceType","visible":true,"width":176,"sort":0},{"id":"MaintCreatedBy","visible":true,"width":171.517,"sort":0},{"id":"MaintCreatedOn","visible":true,"width":101.517,"sort":0},{"id":"ExceptionNotes","visible":true,"width":140.517,"sort":0},{"id":"CurrentEngineHours","visible":true,"width":82.6667,"sort":0},{"id":"CurrentOdometer","visible":true,"width":102.683,"sort":0},{"id":"LastSeenTime","visible":true,"width":135.517,"sort":-1}],"includeDeleted":false,"quickFilters":{"GSEID":"","EquipmentTypeID":"","DriverID":"","OwnerId":"","StationId":"","LastSeenLocationId":"","MaintenanceType":"","LastSeenTime":[null,null]}},"Vijai":{"columns":[{"id":"StationCode","visible":true,"width":117.6923076923077,"sort":0},{"id":"Gse","visible":true,"width":85.7875,"sort":0},{"id":"GseType","visible":true,"width":73.75,"sort":0},{"id":"CurrentEngineHours","visible":true,"width":94.6667,"sort":0},{"id":"EngineStatus","visible":true,"width":42.30769230769231,"sort":0},{"id":"OperatingStatus","visible":true,"width":42.30769230769231,"sort":0},{"id":"Battery","visible":true,"width":42.30769230769231,"sort":0},{"id":"MV","visible":true,"width":124.3,"sort":0},{"id":"CurrentSpeed","visible":true,"width":117.6923076923077,"sort":0},{"id":"FuelLevel","visible":true,"width":143.3,"sort":0},{"id":"LastSeenLocation","visible":true,"width":299.217,"sort":0},{"id":"InMaintenanceUnPlan","visible":true,"width":117.667,"sort":0},{"id":"MaintCreatedBy","visible":true,"width":171.53846153846152,"sort":0},{"id":"MaintCreatedOn","visible":true,"width":101.53846153846153,"sort":0},{"id":"LastSeenTime","visible":true,"width":133.5,"sort":-1},{"id":"Acceleration","visible":true,"width":42.30769230769231,"sort":0},{"id":"BrakingEvents","visible":true,"width":42.30769230769231,"sort":0},{"id":"Hct","visible":true,"width":42.30769230769231,"sort":0},{"id":"Lop","visible":true,"width":42.30769230769231,"sort":0}],"includeDeleted":false,"quickFilters":{"GSEID":"","EquipmentTypeID":"","DriverID":"","OwnerId":"","StationId":"","LastSeenLocationId":"","MaintenanceType":"","LastSeenTime":[null,null]}}}
3	69	UserPreferenceStorage	GridSettings::TrackIT.GSE.GSEStatusGrid	{"columns":[{"id":"Gse","visible":true,"width":83.8125,"sort":0},{"id":"GseType","visible":true,"width":90.75,"sort":0},{"id":"OperatingStatus","visible":true,"width":42.30769230769231,"sort":0},{"id":"Battery","visible":true,"width":60.25,"sort":0},{"id":"MV","visible":true,"width":80.25,"sort":0},{"id":"FuelLevel","visible":true,"width":132.266,"sort":0},{"id":"CurrentEngineHours","visible":true,"width":117.672,"sort":0},{"id":"NextMaintOn","visible":true,"width":117.672,"sort":0},{"id":"InMaintenanceUnPlan","visible":true,"width":117.672,"sort":0},{"id":"MaintCreatedBy","visible":true,"width":171.531,"sort":0},{"id":"MaintCreatedOn","visible":true,"width":159.531,"sort":0},{"id":"LastSeenTime","visible":true,"width":123.525,"sort":-1}],"includeDeleted":false,"quickFilters":{"GSEID":["2359"],"EquipmentTypeID":"","OwnerId":"","StationId":"","MaintenanceType":"","LastSeenTime":[null,null],"LastSeenLocation":"","OperatorName":""}}

```

### TABLE: `dbo.UserRoles`

```sql
CREATE TABLE [dbo].[UserRoles] (
  [UserRoleId] BIGINT NOT NULL,
  [UserId] INTEGER NOT NULL,
  [RoleId] INTEGER NOT NULL
);
```
Sample Rows:
```text
UserRoleId	UserId	RoleId
43	1	1
46	1	3
4	4	2

```

### TABLE: `dbo.Users`

```sql
CREATE TABLE [dbo].[Users] (
  [UserId] INTEGER NOT NULL,
  [Username] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [DisplayName] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [Email] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Source] NVARCHAR(4) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [PasswordHash] NVARCHAR(86) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [PasswordSalt] NVARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [LastDirectoryUpdate] DATETIME,
  [UserImage] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [InsertDate] DATETIME NOT NULL,
  [InsertUserId] INTEGER NOT NULL,
  [UpdateDate] DATETIME,
  [UpdateUserId] INTEGER,
  [IsActive] SMALLINT NOT NULL,
  [MobilePhoneNumber] NVARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantId] INTEGER NOT NULL,
  [TwoFactorEnabled] BIT NOT NULL,
  [AccessKey] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [CreatedBy] INTEGER,
  [TwoFactorData] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [MobilePhoneVerified] BIT,
  [TwoFactorAuth] INTEGER
);
```
Sample Rows:
```text
UserId	Username	DisplayName	Email	Source	PasswordHash	PasswordSalt	LastDirectoryUpdate	UserImage	InsertDate	InsertUserId	UpdateDate	UpdateUserId	IsActive	MobilePhoneNumber	TenantId	TwoFactorEnabled	AccessKey	CreatedBy	TwoFactorData	MobilePhoneVerified	TwoFactorAuth
1	admin	admin	admin@trackit.com	site	6CC8sD5QLBEhv0dFblzMIS+K/nFpXBgDT+6DpBDfGk0yC0xzZKIu/BYj7gcH6IQ+z+6xJKk4FIXPPe/AGV9hyg	4wg26	None	UserImage/00000/00000001_gj4oazslrfp4i.jpg	2014-01-01 00:00:00	1	2025-09-19 17:42:50.953000	1	1	+971588832620	1	False	hJjwycI0fL1	None	None	False	None
4	technician	Technician	None	site	wbr6J8ZNElZkRFjXQ4tfrlU5F1n7JbUZY5el9litA5nLmWd7gTP3tOfik54yiCS0GeyiaJBxHm/6Z0W/4A+Hyg	go4nv	None	UserImage/00000/00000004_ug3w2ev7kfsj2.jpg	2021-08-03 16:38:52.473000	1	2025-03-05 05:18:17.423000	1	1	None	1	False	None	None	None	None	None
5	support	Team	support@trackit.aero	sign	+j0Zdcm/B842zH2G/SZSgQ3uoNy+oEeUnkBczmXqZQrMdRKFd2hiNI8BWL8E1TaKkLgBRyQoDnhob6JqR1bxxw	6jq2k	None	None	2021-08-16 19:13:47.183000	1	2025-06-18 07:44:34.030000	1	1	None	45	False	None	None	None	None	None

```

### TABLE: `dbo.UserStation`

```sql
CREATE TABLE [dbo].[UserStation] (
  [Id] INTEGER NOT NULL,
  [UserId] INTEGER NOT NULL,
  [StationId] INTEGER NOT NULL
);
```
Sample Rows:
```text
Id	UserId	StationId
1	45	2
2	42	1
3	50	3

```

### TABLE: `dbo.UserWidget`

```sql
CREATE TABLE [dbo].[UserWidget] (
  [UserWidgetId] INTEGER NOT NULL,
  [WidgetId] INTEGER,
  [OrderId] INTEGER,
  [UserId] INTEGER
);
```
Sample Rows:
```text
UserWidgetId	WidgetId	OrderId	UserId
13	1	1	2
35	1	1	13
36	2	2	13

```

### TABLE: `dbo.UtilizationHistory`

```sql
CREATE TABLE [dbo].[UtilizationHistory] (
  [Id] INTEGER NOT NULL,
  [TStamp] DATETIME,
  [LocationID] INTEGER,
  [Utilization] INTEGER,
  [TotalCount] INTEGER
);
```
Sample Rows:
```text
Id	TStamp	LocationID	Utilization	TotalCount
1	2025-02-24 17:45:00.893000	1255	1	7
2	2025-02-24 18:00:00.340000	1255	1	7
3	2025-02-24 18:00:00.340000	1256	0	1

```

### TABLE: `dbo.VersionInfo`

```sql
CREATE TABLE [dbo].[VersionInfo] (
  [Version] BIGINT NOT NULL,
  [AppliedOn] DATETIME,
  [Description] NVARCHAR(1024) COLLATE "SQL_Latin1_General_CP1_CI_AS"
);
```
Sample Rows:
```text
Version	AppliedOn	Description
20141103140000	2021-07-29 09:36:29	DefaultDB_20141103_1400_Initial
20141111113000	2021-07-29 09:36:31	DefaultDB_20141111_1130_Permissions
20160515072600	2021-07-29 09:36:32	DefaultDB_20160515_0726_UserPreferences

```

### TABLE: `dbo.Voltage`

```sql
CREATE TABLE [dbo].[Voltage] (
  [AssetNo] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [LowVoltage] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [UnderVoltage] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [OverVoltage] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS"
);
```
Sample Rows:
```text
AssetNo	LowVoltage	UnderVoltage	OverVoltage
415	11.8	11	14.8
420	11.8	11	14.8
405	11.8	11	14.8

```

### TABLE: `dbo.WarehouseMaster`

```sql
CREATE TABLE [dbo].[WarehouseMaster] (
  [WarehouseId] INTEGER NOT NULL,
  [WarehouseCode] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [WarehouseName] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Image] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
WarehouseId	WarehouseCode	WarehouseName	Image	TenantId
1	WH01	Main Warehouse	WarehouseMaster/00000/00000001_f7vsqqu3jajgg.png	1
3	WH01	Main Warehouse	WarehouseMaster/00000/00000001_f7vsqqu3jajgg.png	28
8	WC2	WN2	WarehouseMaster/00000/00000008_xstyxjbyori3s.png	1

```

### TABLE: `dbo.WheelchairMaster`

```sql
CREATE TABLE [dbo].[WheelchairMaster] (
  [WheelchairId] INTEGER NOT NULL,
  [TagId] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [SerialNumber] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [WheelchairTypeId] INTEGER,
  [ServiceDate] DATETIME,
  [FirstSeenTime] DATETIME,
  [LastSeenTime] DATETIME,
  [LastSeenLocation] INTEGER,
  [Status] INTEGER,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
WheelchairId	TagId	SerialNumber	WheelchairTypeId	ServiceDate	FirstSeenTime	LastSeenTime	LastSeenLocation	Status	TenantId
1	T-01	SN-893764	1	2022-02-11 00:00:00	2022-02-11 00:00:00	None	None	1	1
2	T-02	SN-893765	1	2001-05-01 00:00:00	2022-02-21 00:00:00	2022-02-08 00:00:00	3	1	1
3	TAG1	33333	3	2022-10-22 00:00:00	None	None	None	2	1

```

### TABLE: `dbo.WheelchairTypeMaster`

```sql
CREATE TABLE [dbo].[WheelchairTypeMaster] (
  [WheelchairTypeId] INTEGER NOT NULL,
  [Code] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Name] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
WheelchairTypeId	Code	Name	TenantId
1	WTC01	WTN01	1
2	WTC01	WTN01	28
3	WTC1	WTN1	1

```

### TABLE: `dbo.wlog_Currency`

```sql
CREATE TABLE [dbo].[wlog_Currency] (
  [CurrencyCode] NVARCHAR(3) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL
);
```
Sample Rows:
```text
CurrencyCode
EUR
USD

```

### TABLE: `dbo.wlog_Customer`

```sql
CREATE TABLE [dbo].[wlog_Customer] (
  [CustomerId] INTEGER NOT NULL,
  [UserId] INTEGER,
  [Name] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [HourlyRate] DECIMAL(18, 2) NOT NULL,
  [CurrencyCode] NVARCHAR(3) COLLATE "SQL_Latin1_General_CP1_CI_AS"
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `dbo.wlog_Employee`

```sql
CREATE TABLE [dbo].[wlog_Employee] (
  [EmployeeId] INTEGER NOT NULL,
  [UserId] INTEGER,
  [Name] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `dbo.wlog_EmployeePricing`

```sql
CREATE TABLE [dbo].[wlog_EmployeePricing] (
  [EmployeePricingId] INTEGER NOT NULL,
  [EmployeeId] INTEGER NOT NULL,
  [CustomerId] INTEGER NOT NULL,
  [ProjectId] INTEGER,
  [HourlyRate] DECIMAL(18, 2) NOT NULL,
  [CurrencyCode] NVARCHAR(3) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `dbo.wlog_Invoice`

```sql
CREATE TABLE [dbo].[wlog_Invoice] (
  [InvoiceId] INTEGER NOT NULL,
  [CustomerId] INTEGER NOT NULL,
  [InvoiceNo] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [Date] DATETIME,
  [Amount] DECIMAL(18, 2),
  [CurrencyCode] NVARCHAR(3) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Notes] NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS"
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `dbo.wlog_Project`

```sql
CREATE TABLE [dbo].[wlog_Project] (
  [ProjectId] INTEGER NOT NULL,
  [CustomerId] INTEGER NOT NULL,
  [Name] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [EndCustomer] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [HourlyRate] DECIMAL(18, 2),
  [CurrencyCode] NVARCHAR(3) COLLATE "SQL_Latin1_General_CP1_CI_AS"
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `dbo.wlog_WorkLog`

```sql
CREATE TABLE [dbo].[wlog_WorkLog] (
  [WorkLogId] INTEGER NOT NULL,
  [ProjectId] INTEGER NOT NULL,
  [EmployeeId] INTEGER NOT NULL,
  [Tasks] NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Description] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [StartDate] DATETIME NOT NULL,
  [EndDate] DATETIME NOT NULL,
  [Price] DECIMAL(18, 2) NOT NULL,
  [CurrencyCode] NVARCHAR(3) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [InvoiceId] INTEGER
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `dbo.WorkStationMaster`

```sql
CREATE TABLE [dbo].[WorkStationMaster] (
  [WSId] INTEGER NOT NULL,
  [WSNumber] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [WSSize] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
WSId	WSNumber	WSSize	TenantId
1	WS-01	50cm	1
2	WS-01	50cm	28
3	WSN1	12	1

```

### TABLE: `dbo.WorkStationSchedule`

```sql
CREATE TABLE [dbo].[WorkStationSchedule] (
  [WSSId] INTEGER NOT NULL,
  [WSId] INTEGER NOT NULL,
  [StartDate] DATETIME,
  [EndDate] DATETIME,
  [OperationType] INTEGER,
  [FlightNumber] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
WSSId	WSId	StartDate	EndDate	OperationType	FlightNumber	TenantId
1	1	2022-01-28 12:40:00	2022-01-28 12:40:00	1	FN-01-0088	1
2	3	2001-05-01 00:00:00	2001-10-01 00:00:00	1	F001	1
4	11	2022-12-20 00:00:00	2022-12-31 00:00:00	1	A320	1

```


## 🧱 TABLES – Schema `gse`

### TABLE: `gse._TrackingDataDaily`

```sql
CREATE TABLE [gse].[_TrackingDataDaily] (
  [TrackingDataDailyId] INTEGER NOT NULL,
  [DeviceID] INTEGER NOT NULL,
  [LastPingTime] DATETIME NOT NULL,
  [TotalPingCount] DECIMAL(20, 2) NOT NULL,
  [LastBatteryLevel] DECIMAL(20, 2) NOT NULL,
  [LastFuelLevel] DECIMAL(20, 2),
  [LastValidLatitude] DECIMAL(20, 2),
  [LastValidLongitude] DECIMAL(20, 2),
  [LastValidHeading] DECIMAL(20, 2),
  [LastValidSpeedKPH] DECIMAL(20, 2),
  [LastGPSTimestamp] DATETIME,
  [LastEventStatusCode] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [LastEventTimestamp] DATETIME,
  [LastLat] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [LastLang] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Status1] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Status2] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Status3] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.AircraftGSE`

```sql
CREATE TABLE [gse].[AircraftGSE] (
  [MappingId] INTEGER NOT NULL,
  [Make] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Model] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Assigned] INTEGER,
  [ResourceCode] INTEGER,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
MappingId	Make	Model	Assigned	ResourceCode	TenantId
1077	TLD	TMX-50-E	None	396	1
1078	TLD	TMX-350 -E	None	396	1
1079	TLD	TMX-250-E	None	396	1

```

### TABLE: `gse.AircraftMaster`

```sql
CREATE TABLE [gse].[AircraftMaster] (
  [AircraftId] INTEGER NOT NULL,
  [IATACode] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ICAOCode] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [AircraftModel] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [AircraftCategory] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
AircraftId	IATACode	ICAOCode	AircraftModel	AircraftCategory	TenantId
1	A4F	A124	Antonov AN-124 Ruslan	Wide Bidy	1
2	A40	A140	Antonov AN-140	Narrow Body	1
3	A81	A148	Antonov An-148	Narrow Body	1

```

### TABLE: `gse.AirlineMaster`

```sql
CREATE TABLE [gse].[AirlineMaster] (
  [AirlineId] INTEGER NOT NULL,
  [Code] NVARCHAR(2) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Name] NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
AirlineId	Code	Name	TenantId
1	VX	Aces	1
2	XQ	Action Airlines	1
3	WZ	Acvilla Air	1

```

### TABLE: `gse.AssetTrips`

```sql
CREATE TABLE [gse].[AssetTrips] (
  [TripID] INTEGER NOT NULL,
  [AssetID] INTEGER,
  [StartTime] DATETIME,
  [EndTime] DATETIME,
  [StartDeviceLogID] INTEGER,
  [StopDeviceLogID] INTEGER,
  [TotalDistance] FLOAT,
  [MaxSpeed] INTEGER,
  [AvgSpeed] INTEGER,
  [Operator] NVARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [IdleDurationSecs] INTEGER,
  [TotalDriveTimeSecs] INTEGER,
  [TotalWorkTimeSecs] INTEGER,
  [cInfringe] INTEGER,
  [cSpeeding] INTEGER,
  [cFaults] INTEGER,
  [cHB] INTEGER,
  [cHA] INTEGER,
  [isUpdated] BIT,
  [TenantId] INTEGER
);
```
Sample Rows:
```text
TripID	AssetID	StartTime	EndTime	StartDeviceLogID	StopDeviceLogID	TotalDistance	MaxSpeed	AvgSpeed	Operator	IdleDurationSecs	TotalDriveTimeSecs	TotalWorkTimeSecs	cInfringe	cSpeeding	cFaults	cHB	cHA	isUpdated	TenantId
1	67	2022-06-25 13:48:00.010000	2022-06-25 14:02:38	0	0	8.74239106719992	47	0		123	747	0	0	0	0	0	0	True	20
2	67	2022-06-25 14:04:00	2022-06-25 14:05:02.010000	0	0	0.0	0	0		62	0	0	0	0	0	0	0	True	20
3	67	2022-06-25 14:05:11	2022-06-25 14:05:31	0	0	0.0	0	0		20	0	0	0	0	0	0	0	True	20

```

### TABLE: `gse.AVPHistory`

```sql
CREATE TABLE [gse].[AVPHistory] (
  [AVPHistoryID] INTEGER NOT NULL,
  [GSEID] INTEGER NOT NULL,
  [AVPNumber] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [IssueDate] DATETIME NOT NULL,
  [ExpiryDate] DATETIME NOT NULL,
  [IssuedBy] NVARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [StationID] INTEGER,
  [IsCurrent] BIT NOT NULL,
  [CreatedDate] DATETIME NOT NULL,
  [CreatedBy] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
AVPHistoryID	GSEID	AVPNumber	IssueDate	ExpiryDate	IssuedBy	StationID	IsCurrent	CreatedDate	CreatedBy	TenantId
1	2426	123456	2025-08-15 00:00:00	2025-09-30 00:00:00	Test	18	False	2025-08-15 16:50:31.557000	79	48
3	2427	P2-1234	2025-08-01 00:00:00	2025-09-30 00:00:00	Test 3	18	True	2025-08-18 14:08:38.993000	79	48
4	2426	P1-1234	2025-07-02 00:00:00	2025-09-30 00:00:00	Test 2	18	True	2025-08-18 14:47:01.483000	79	48

```

### TABLE: `gse.Category`

```sql
CREATE TABLE [gse].[Category] (
  [CategoryID] INTEGER NOT NULL,
  [CategoryName] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [CategoryCode] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [CompanyID] INTEGER,
  [CompanyName] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [AssetType] INTEGER,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
CategoryID	CategoryName	CategoryCode	CompanyID	CompanyName	AssetType	TenantId
9	Non Motorized GSE	NME	1	TrackIT	150	5
51	Non Motorized GSE	NME	None	None	300	5
52	Non Motorized GSE	NME	None	None	149	5

```

### TABLE: `gse.ContractEquipment`

```sql
CREATE TABLE [gse].[ContractEquipment] (
  [TID] INTEGER NOT NULL,
  [ContractFlightId] INTEGER,
  [ContractID] INTEGER,
  [AssetTypeID] INTEGER,
  [AssetCount] INTEGER,
  [ActivityType] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [StartPhase] VARCHAR(2) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [StartOffset] INTEGER,
  [EndPhase] VARCHAR(2) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [EndOffset] INTEGER,
  [TenantId] INTEGER,
  [ContractVerId] INTEGER,
  [CreatedDate] DATETIME,
  [CreatedBy] INTEGER,
  [EngagementPeriod] INTEGER,
  [Status] INTEGER
);
```
Sample Rows:
```text
TID	ContractFlightId	ContractID	AssetTypeID	AssetCount	ActivityType	StartPhase	StartOffset	EndPhase	EndOffset	TenantId	ContractVerId	CreatedDate	CreatedBy	EngagementPeriod	Status
1	1	1	1532	1	2	1	-2	2	2	17	1	2023-05-06 10:01:54.640000	1	None	1

```

### TABLE: `gse.ContractFlight`

```sql
CREATE TABLE [gse].[ContractFlight] (
  [ContractFlightId] INTEGER NOT NULL,
  [AirlineId] INTEGER,
  [FlightDuration] INTEGER,
  [MissionType] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [AircraftId] INTEGER,
  [ContractId] INTEGER,
  [TenantId] INTEGER,
  [ContractVerId] INTEGER,
  [CreatedDate] DATETIME,
  [CreatedBy] INTEGER,
  [Status] INTEGER
);
```
Sample Rows:
```text
ContractFlightId	AirlineId	FlightDuration	MissionType	AircraftId	ContractId	TenantId	ContractVerId	CreatedDate	CreatedBy	Status
1	None	20	3	354	1	17	1	2023-05-06 08:00:27.390000	1	1

```

### TABLE: `gse.Contracts`

```sql
CREATE TABLE [gse].[Contracts] (
  [ContractID] INTEGER NOT NULL,
  [ContractName] VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ContractType] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [StartDate] DATETIME,
  [EndDate] DATETIME,
  [InvoicingPeriod] INTEGER,
  [AMCStartDate] DATETIME,
  [AMCEndDate] DATETIME,
  [AMCType] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantId] INTEGER,
  [Status] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [CreatedDate] DATETIME,
  [CreatedBy] INTEGER
);
```
Sample Rows:
```text
ContractID	ContractName	ContractType	StartDate	EndDate	InvoicingPeriod	AMCStartDate	AMCEndDate	AMCType	TenantId	Status	CreatedDate	CreatedBy
1	Test	None	2025-09-20 00:00:00	2025-12-31 00:00:00	None	None	None	None	1	Planned	2023-05-06 07:59:58.177000	1

```

### TABLE: `gse.ContractVersion`

```sql
CREATE TABLE [gse].[ContractVersion] (
  [ContractVerId] INTEGER NOT NULL,
  [ContractId] INTEGER NOT NULL,
  [VersionNo] INTEGER,
  [VersionDescription] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [CreatedDate] DATETIME NOT NULL,
  [CreatedBy] INTEGER NOT NULL,
  [ContractFlightId] INTEGER
);
```
Sample Rows:
```text
ContractVerId	ContractId	VersionNo	VersionDescription	CreatedDate	CreatedBy	ContractFlightId
1	1	1	New contract is created	2023-05-06 07:59:58.213000	1	1

```

### TABLE: `gse.DashBoardChartsDaily`

```sql
CREATE TABLE [gse].[DashBoardChartsDaily] (
  [DashBoardChartsDailyId] INTEGER NOT NULL,
  [DeviceID] INTEGER NOT NULL,
  [DeviceName] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [FuelConsumption] DECIMAL(20, 2) NOT NULL,
  [Mileage] DECIMAL(20, 2),
  [EngineHours] DECIMAL(20, 2),
  [AverageSpeed] DECIMAL(20, 2),
  [MaximumSpeed] DECIMAL(20, 2),
  [Idling] DECIMAL(20, 2),
  [Trips] DECIMAL(20, 2),
  [Stays] DECIMAL(20, 2),
  [MessageOn] DATETIME,
  [LastPositionLocation] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Speed] INTEGER
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.DashBoardSummary`

```sql
CREATE TABLE [gse].[DashBoardSummary] (
  [DashBoardSummaryId] INTEGER NOT NULL,
  [DeviceID] INTEGER NOT NULL,
  [DeviceName] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [MessageOn] DATETIME,
  [ConnectionState] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [LastMessageOn] DATETIME,
  [LastPositionLocation] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Speed] INTEGER
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.DemandForecasting`

```sql
CREATE TABLE [gse].[DemandForecasting] (
  [AutoID] INTEGER NOT NULL,
  [GSETypeID] INTEGER,
  [GSETypeName] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TimeSlot] DATETIME,
  [Count] INTEGER,
  [TenantId] INTEGER
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.DeviceDetails`

```sql
CREATE TABLE [gse].[DeviceDetails] (
  [DeviceID] INTEGER NOT NULL,
  [InstallTime] DATETIME,
  [ExpirationTime] DATETIME,
  [SimPhoneNo] NVARCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [SimID] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [SMSEmail] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [IMEINumber] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [CompanyID] INTEGER,
  [CompanyName] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TimeZoneId] INTEGER,
  [DeviceType] INTEGER,
  [LastLat] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [LastLang] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [LastSeenTime] DATETIME,
  [LastSeenLocation] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [HeadingOffset] INTEGER,
  [TenantId] INTEGER NOT NULL,
  [DriverID] VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [HDOP] INTEGER,
  [Input0] FLOAT,
  [Input1] FLOAT,
  [Input2] FLOAT,
  [Input3] FLOAT,
  [Input4] FLOAT,
  [Input5] FLOAT,
  [Input6] FLOAT,
  [Input7] FLOAT,
  [Input8] FLOAT,
  [Input9] FLOAT,
  [Output0] FLOAT,
  [Output1] FLOAT,
  [Output2] FLOAT,
  [Output3] FLOAT,
  [Output4] FLOAT,
  [Output5] FLOAT,
  [AI0] FLOAT,
  [AI1] FLOAT,
  [AI2] FLOAT,
  [AI3] FLOAT,
  [BLEList] VARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [GX] FLOAT,
  [GY] FLOAT,
  [GZ] FLOAT,
  [Heading] INTEGER,
  [MV] FLOAT,
  [BV] FLOAT,
  [GSMSignal] FLOAT,
  [RPM] INTEGER,
  [CellID] VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Speed] INTEGER,
  [Odometer] FLOAT,
  [EngineHours] FLOAT,
  [EngineLoad] FLOAT,
  [EngineTemp] FLOAT,
  [FuelUsed] FLOAT,
  [FuelLevel] FLOAT,
  [IntakeTemp] FLOAT,
  [MassAirFlow] FLOAT,
  [MalfunctionIndicator] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ManifoldPressure] FLOAT,
  [ThrottlePosition] FLOAT,
  [VINNumber] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [IsEngineSignal] BIT,
  [IsHCT] BIT,
  [IsLOP] BIT,
  [IsWork] BIT,
  [EnginePort] INTEGER,
  [HCTPort] INTEGER,
  [LOPPort] INTEGER,
  [Work1Port] INTEGER,
  [Work2Port] INTEGER,
  [Work3Port] INTEGER,
  [Work4Port] INTEGER,
  [Work1Name] VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Work2Name] VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Work3Name] VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Work4Name] VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [FuelPort] INTEGER,
  [FuelType] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [EngineSignalType] INTEGER,
  [FuelSlope] FLOAT,
  [FuelOffset] FLOAT,
  [LowVoltage] FLOAT,
  [UnderVoltage] FLOAT,
  [OverVoltage] FLOAT,
  [isCANbus] BIT
);
```
Sample Rows:
```text
DeviceID	InstallTime	ExpirationTime	SimPhoneNo	SimID	SMSEmail	IMEINumber	CompanyID	CompanyName	TimeZoneId	DeviceType	LastLat	LastLang	LastSeenTime	LastSeenLocation	HeadingOffset	TenantId	DriverID	HDOP	Input0	Input1	Input2	Input3	Input4	Input5	Input6	Input7	Input8	Input9	Output0	Output1	Output2	Output3	Output4	Output5	AI0	AI1	AI2	AI3	BLEList	GX	GY	GZ	Heading	MV	BV	GSMSignal	RPM	CellID	Speed	Odometer	EngineHours	EngineLoad	EngineTemp	FuelUsed	FuelLevel	IntakeTemp	MassAirFlow	MalfunctionIndicator	ManifoldPressure	ThrottlePosition	VINNumber	IsEngineSignal	IsHCT	IsLOP	IsWork	EnginePort	HCTPort	LOPPort	Work1Port	Work2Port	Work3Port	Work4Port	Work1Name	Work2Name	Work3Name	Work4Name	FuelPort	FuelType	EngineSignalType	FuelSlope	FuelOffset	LowVoltage	UnderVoltage	OverVoltage	isCANbus
398	2022-06-08 00:00:00	2030-10-08 00:00:00	866907052433223	P263	None	866907052433223	1	TrackIT	45	2675	24.9559949	46.707685	2026-01-05 12:51:58	مطار الملك خالد الدولي	0	20		0	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None		0.0	0.0	0.0	0	0.0	0.0	0.0	0		0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	None	None	None	None		True	False	False	False	1	0	0	0	0	0	0	None	None	None	None	0	None	2	0.0	0.0	9.0	11.0	15.0	False
399	2022-06-08 00:00:00	2030-10-08 00:00:00	866907051387511	P261	None	866907051387511	1	TrackIT	45	2675	30.9844583	41.0406333	2026-01-02 18:35:18.010000	الفيصلية	0	20		0	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None		0.0	0.0	0.0	0	0.0	0.0	0.0	0		0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	None	None	None	None		True	False	False	False	1	0	0	0	0	0	0	None	None	None	None	0	None	2	0.0	0.0	9.0	11.0	15.0	False
401	2022-06-16 00:00:00	2030-10-16 00:00:00	866907050773786	P290	None	866907050773786	1	TrackIT	45	2675	24.9691483	46.6937833	2026-01-05 09:43:41	Satco Bto Office	0	20		0	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None		0.0	0.0	0.0	0	0.0	0.0	0.0	0		0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	None	None	None	None		True	False	False	False	1	0	0	0	0	0	0	None	None	None	None	0	None	2	0.0	0.0	9.0	11.0	15.0	False

```

### TABLE: `gse.DeviceEvents`

```sql
CREATE TABLE [gse].[DeviceEvents] (
  [Id] INTEGER NOT NULL,
  [DeviceID] INTEGER,
  [EventType] INTEGER,
  [EventTime] DATETIME,
  [ELatitude] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ELongitude] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ELocationID] INTEGER,
  [EventData] VARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [isAlarm] BIT,
  [isDismissed] BIT,
  [DismissedAt] DATETIME,
  [DismissedBy] INTEGER,
  [AssetID] INTEGER,
  [LogID] INTEGER,
  [EngineStatus] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [OpStatus] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [AuxStatus] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [geom] NULL,
  [HA] VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [HB] VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [MV] FLOAT,
  [BV] FLOAT,
  [Speed] FLOAT,
  [FuelLevel] INTEGER,
  [Heading] INTEGER,
  [HCT] INTEGER,
  [LOP] INTEGER,
  [LastSeen] BIGINT,
  [LastSeenBefore] BIGINT,
  [OverSpeed] INTEGER
);
```
Sample Rows:
```text
Id	DeviceID	EventType	EventTime	ELatitude	ELongitude	ELocationID	EventData	isAlarm	isDismissed	DismissedAt	DismissedBy	AssetID	LogID	EngineStatus	OpStatus	AuxStatus	geom	HA	HB	MV	BV	Speed	FuelLevel	Heading	HCT	LOP	LastSeen	LastSeenBefore	OverSpeed
53	442	34	2023-04-28 10:38:40	24.966175	46.6978816	0	51 kmp/h Limit:50 km/h	False	False	None	None	101	0	ON_VA	DRIVE	UNKNOWN	None	0	0	13.9	0.0	51.0	0	306	None	None	1682678320	1682678318	0
264	443	34	2023-04-28 10:42:01	24.9664966	46.697565	0	53 kmp/h Limit:50 km/h	False	False	None	None	102	0	ON_VA	DRIVE	UNKNOWN	None	0	3	13.8	0.0	53.0	0	326	None	None	1682678521	1682678519	0
608	425	34	2023-04-28 11:37:04	24.92167	46.681035	227	52 kmp/h Limit:50 km/h	False	False	None	None	88	0	ON_VA	DRIVE	UNKNOWN	None	0	0	13.6	0.0	52.0	0	151	None	None	1682681824	1682681822	0

```

### TABLE: `gse.DeviceEventsTemp`

```sql
CREATE TABLE [gse].[DeviceEventsTemp] (
  [Id] INTEGER NOT NULL,
  [DeviceID] INTEGER,
  [EventType] INTEGER,
  [EventTime] DATETIME,
  [ELatitude] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ELongitude] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ELocationID] INTEGER,
  [EventData] VARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [isAlarm] BIT,
  [isDismissed] BIT,
  [DismissedAt] DATETIME,
  [DismissedBy] INTEGER,
  [AssetID] INTEGER
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.DeviceLog`

```sql
CREATE TABLE [gse].[DeviceLog] (
  [Id] INTEGER NOT NULL,
  [DeviceID] INTEGER,
  [Latitude] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Longitude] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Heading] INTEGER,
  [ReportID] INTEGER,
  [Odometer] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Speed] FLOAT,
  [DriverID] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TempSensor1] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TempSensor2] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TxtMsg] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [CIString] VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TStamp] DATETIME,
  [GPSTime] DATETIME,
  [Inputs] INTEGER,
  [AssetID] INTEGER,
  [OpMode] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [LocationID] INTEGER
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.DevicePeriodEvents`

```sql
CREATE TABLE [gse].[DevicePeriodEvents] (
  [Id] INTEGER NOT NULL,
  [DeviceID] INTEGER,
  [EventType] INTEGER,
  [StartTime] DATETIME,
  [EndTime] DATETIME,
  [StartLat] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [StartLong] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [StartLocID] INTEGER,
  [EndLat] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [EndLong] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [EndLocID] INTEGER,
  [EventData] VARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [AssetID] INTEGER,
  [InsertDate] DATETIME
);
```
Sample Rows:
```text
Id	DeviceID	EventType	StartTime	EndTime	StartLat	StartLong	StartLocID	EndLat	EndLong	EndLocID	EventData	AssetID	InsertDate
4	498	40	2023-04-28 10:35:09.253000	2023-04-28 10:35:19.253000	18.3078302	-15.962907	0	18.3078302	-15.962907	0	UNLOAD	46	2023-04-28 10:35:20.620000
5	498	6	2023-04-28 10:35:19.253000	2023-04-28 10:35:29.257000	18.3078302	-15.962907	0	18.3078302	-15.962907	0	UNKNOWN	46	2023-04-28 10:35:30.433000
6	498	6	2023-04-28 10:35:29.257000	2023-04-28 10:35:39.257000	18.3078302	-15.962907	0	18.3078302	-15.962907	0	UNKNOWN	46	2023-04-28 10:35:40.387000

```

### TABLE: `gse.DeviceThreshold`

```sql
CREATE TABLE [gse].[DeviceThreshold] (
  [Id] INTEGER NOT NULL,
  [DeviceTypeID] INTEGER,
  [SignalType] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ShouldRemainForSecs] INTEGER,
  [ConditionExpression] VARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [LowValue] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [HighValue] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TriggerOnLow] BIT,
  [TriggerOnHigh] BIT,
  [TriggerOnToggle] BIT,
  [EventID] INTEGER
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.DriverActivityDaily`

```sql
CREATE TABLE [gse].[DriverActivityDaily] (
  [DriverActivityDailyDailyId] INTEGER NOT NULL,
  [DriverID] INTEGER NOT NULL,
  [Beginning] DATETIME,
  [End] DATETIME NOT NULL,
  [TotalDuration] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [DrivingDuration] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [IdleDuration] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Mileage] DECIMAL(20, 2),
  [MessageOn] DATETIME,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.DriverAllocation`

```sql
CREATE TABLE [gse].[DriverAllocation] (
  [DriverAllocationId] INTEGER NOT NULL,
  [DriverID] INTEGER NOT NULL,
  [AssetId] INTEGER,
  [StartDate] DATETIME,
  [EndDate] DATETIME,
  [Active] BIT NOT NULL,
  [TenantId] INTEGER NOT NULL,
  [ResourceCode] INTEGER
);
```
Sample Rows:
```text
DriverAllocationId	DriverID	AssetId	StartDate	EndDate	Active	TenantId	ResourceCode
1	9	89	None	None	True	20	None
2	11	78	2023-04-12 00:00:00	2023-04-13 00:00:00	True	20	None
3	11	79	2023-04-25 00:00:00	2023-04-26 00:00:00	True	20	None

```

### TABLE: `gse.DriverAssessment`

```sql
CREATE TABLE [gse].[DriverAssessment] (
  [DriverAssessmentId] INTEGER NOT NULL,
  [DriverID] INTEGER NOT NULL,
  [DriverName] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [VehicleID] INTEGER NOT NULL,
  [VehicleName] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [Rating] INTEGER,
  [Violations] INTEGER,
  [Duration] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Mileage] DECIMAL(20, 2),
  [Trips] INTEGER,
  [MessageOn] DATETIME,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.DriverDetails`

```sql
CREATE TABLE [gse].[DriverDetails] (
  [DriverID] INTEGER NOT NULL,
  [DriverName] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [DisplayName] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [DoB] DATETIME,
  [LicenseNo] NVARCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [LicenseType] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [Condition] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [IssuersCountry] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ExpiryDate] DATETIME,
  [BadgeID] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [CardID] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Email] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [Phone] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [IMEINumber] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [CompanyID] INTEGER,
  [CompanyName] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ResourceCode] INTEGER,
  [ADPDate] DATETIME,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
DriverID	DriverName	DisplayName	DoB	LicenseNo	LicenseType	Condition	IssuersCountry	ExpiryDate	BadgeID	CardID	Email	Phone	IMEINumber	CompanyID	CompanyName	ResourceCode	ADPDate	TenantId
1	John	John	1985-02-02 00:00:00	23432254	Heavy Vehicles	0	Dubai	2022-02-02 00:00:00	002548	324234322	info@gse.com	234234232	234324435343	1	TrackIT	None	None	5
2	Samuel	Samuel	1986-01-05 00:00:00	23432255	Heavy Vehicles	0	Dubai	2023-01-05 00:00:00	002546	353432155	info@gse.com	254785455	231456875784	1	TrackIT	None	None	5
3	Joseph	Joseph	1985-03-07 00:00:00	23455878	Heavy Vehicles	0	Dubai	2022-03-07 00:00:00	3254125	325478489	info@gse.com	245647885	265478954212	1	TrackIT	73	None	5

```

### TABLE: `gse.DriverGroupAllocation`

```sql
CREATE TABLE [gse].[DriverGroupAllocation] (
  [DriverGroupId] INTEGER NOT NULL,
  [DriverID] INTEGER NOT NULL,
  [TenantId] INTEGER NOT NULL,
  [IsSync] BIT,
  [GSEGroupId] INTEGER
);
```
Sample Rows:
```text
DriverGroupId	DriverID	TenantId	IsSync	GSEGroupId
1	12	20	None	2
2	12	20	None	1
3	9	20	None	2

```

### TABLE: `gse.DriverGSEType`

```sql
CREATE TABLE [gse].[DriverGSEType] (
  [DriverGSETypeId] INTEGER NOT NULL,
  [DriverId] INTEGER NOT NULL,
  [GSETypeID] INTEGER NOT NULL
);
```
Sample Rows:
```text
DriverGSETypeId	DriverId	GSETypeID
6	67	919
9	9	919
37	235	3080

```

### TABLE: `gse.DrivingLogBook`

```sql
CREATE TABLE [gse].[DrivingLogBook] (
  [DrivingLogBookId] INTEGER NOT NULL,
  [Beginning] DATETIME,
  [End] DATETIME NOT NULL,
  [Duration] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [InitialLocation] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [FinalLocation] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Mileage] DECIMAL(20, 2),
  [DriverID] INTEGER NOT NULL,
  [LastChangesDate] DATETIME,
  [FlightNo] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [MissionID] INTEGER NOT NULL,
  [Notes] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [InitLat] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [InitLang] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.EngagementStandards`

```sql
CREATE TABLE [gse].[EngagementStandards] (
  [StandardId] INTEGER NOT NULL,
  [CategoryCode] INTEGER,
  [Eng_Std_Phase] INTEGER,
  [Eng_Std_BeginType] NVARCHAR(5) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Eng_Std_BeginMint] INTEGER,
  [Eng_Std_EndType] NVARCHAR(5) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Eng_Std_EndMint] INTEGER,
  [ResourceUnits] INTEGER,
  [TenantId] INTEGER NOT NULL,
  [ActivityType] INTEGER
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.EquipmentMaintenanceThresholds`

```sql
CREATE TABLE [gse].[EquipmentMaintenanceThresholds] (
  [ThresholdID] INTEGER NOT NULL,
  [GSEID] INTEGER NOT NULL,
  [MaintenanceTypeID] INTEGER NOT NULL,
  [CustomUsageThreshold] INTEGER
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.EventTypes`

```sql
CREATE TABLE [gse].[EventTypes] (
  [Id] INTEGER NOT NULL,
  [EventName] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [isAlarm] BIT,
  [EventColor] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantId] INTEGER NOT NULL,
  [TriggerOn] VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [EmailMsg] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [SMSMsg] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [RequiredPlaceholders] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS"
);
```
Sample Rows:
```text
Id	EventName	isAlarm	EventColor	TenantId	TriggerOn	EmailMsg	SMSMsg	RequiredPlaceholders
1	Engine ON	False	None	1	None	None	None	None
2	Engine OFF	False	#FF6C6C	1	None	None	None	None
3	Harsh Braking	True	None	1	EveryTime	None	None	None

```

### TABLE: `gse.ExcepFuel`

```sql
CREATE TABLE [gse].[ExcepFuel] (
  [FuelExceptionId] INTEGER NOT NULL,
  [VehicleID] INTEGER NOT NULL,
  [AssetID] INTEGER NOT NULL,
  [GSEType] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [FuelLevel] INTEGER,
  [Status] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [GeoLocation] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ExceptionNotes] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [MessageOn] DATETIME,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.ExcepMaintenance`

```sql
CREATE TABLE [gse].[ExcepMaintenance] (
  [MaintExceptionId] INTEGER NOT NULL,
  [VehicleID] INTEGER NOT NULL,
  [AssetID] INTEGER NOT NULL,
  [DueOnDate] DATETIME,
  [DueDays] INTEGER,
  [MaintenanceStatus] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ExceptionNotes] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [GSEType] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [MessageOn] DATETIME,
  [ServiceDate] DATETIME,
  [Last_Mileage] DECIMAL(20, 2),
  [Last_EngHours] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantId] INTEGER NOT NULL,
  [MaintenanceType] INTEGER,
  [CreatedBy] INTEGER,
  [CreatedOn] DATETIME
);
```
Sample Rows:
```text
MaintExceptionId	VehicleID	AssetID	DueOnDate	DueDays	MaintenanceStatus	ExceptionNotes	GSEType	MessageOn	ServiceDate	Last_Mileage	Last_EngHours	TenantId	MaintenanceType	CreatedBy	CreatedOn
1	26	26	None	None	1	Test	None	2023-04-29 01:05:00	None	None	None	15	1	None	None
26	187	187	None	None	Breakdown		None	2024-03-23 00:00:00	None	None	None	39	5	None	None
27	237	237	None	None	Breakdown		None	2024-03-23 00:00:00	None	None	None	39	5	None	None

```

### TABLE: `gse.ExtractDailySummary02`

```sql
CREATE TABLE [gse].[ExtractDailySummary02] (
  [EventDate] DATE,
  [AssetNo] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [EventName] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantId] INTEGER NOT NULL,
  [TotalTimeInMinutes] INTEGER,
  [EquipmentType] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [EquipmentTypeName] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [StationCode] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [OwnerName] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [YearOfMfg] DATETIME,
  [Make] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [ModelNo] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL
);
```
Sample Rows:
```text
EventDate	AssetNo	EventName	TenantId	TotalTimeInMinutes	EquipmentType	EquipmentTypeName	StationCode	OwnerName	YearOfMfg	Make	ModelNo
2025-08-14	P286 6605 TBB	Engine ON	20	418	MINIBUS	MINIBUS	None	None	None	131	147
2025-08-14	13001	Available	42	423	HLL	High Lift Loader	CGK	Gapura Angkasa	2016-06-01 00:00:00	Air Marrel	LAM7000/L9
2025-08-14	17003	Engine ON	42	203	WSU	Water Service Unit	CGK	Gapura Angkasa	2016-06-01 00:00:00	Vestergaard	WS

```

### TABLE: `gse.FlightEquipmentException`

```sql
CREATE TABLE [gse].[FlightEquipmentException] (
  [Id] INTEGER NOT NULL,
  [FlightId] INTEGER,
  [Exception] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ExceptionType] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Status] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantId] INTEGER,
  [CreatedOn] DATETIME,
  [CreatedBy] INTEGER
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.FlightEquipments`

```sql
CREATE TABLE [gse].[FlightEquipments] (
  [TID] INTEGER NOT NULL,
  [FlightID] INTEGER,
  [ContractTID] INTEGER,
  [AssetID] INTEGER,
  [PlanStart] DATETIME,
  [PlanEnd] DATETIME,
  [ActualStart] DATETIME,
  [ActualEnd] DATETIME,
  [Status] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantId] INTEGER,
  [ContractVerId] INTEGER,
  [SeasonVerId] INTEGER,
  [CreatedDate] DATETIME,
  [CreatedBy] INTEGER,
  [Phase] INTEGER,
  [ContractFlightId] INTEGER
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.FlightMaster`

```sql
CREATE TABLE [gse].[FlightMaster] (
  [MissionID] INTEGER NOT NULL,
  [FlightNo] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Airline] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [AircraftType] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ETA] DATETIME NOT NULL,
  [STD] DATETIME NOT NULL,
  [GateorStand] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Origin] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Destination] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [EngagementStandards] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [MessageOn] DATETIME,
  [DepartureFlightNo] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ATA] DATETIME,
  [ATD] DATETIME,
  [BayNumber] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Remarks] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantId] INTEGER,
  [AircraftId] INTEGER,
  [TunraroundTime] FLOAT
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.FlightPlan`

```sql
CREATE TABLE [gse].[FlightPlan] (
  [FlightPlanID] INTEGER NOT NULL,
  [MissionID] INTEGER NOT NULL,
  [FlightNo] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [MissionType] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [MissionTypeID] NVARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TurnaroundTime] INTEGER,
  [GSEType] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [CountofGSE] INTEGER,
  [EngagementStart] DATETIME,
  [EngagementEnd] DATETIME,
  [TotalDuration] NVARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ParentFlightPlanID] INTEGER,
  [MessageOn] DATETIME,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.FlightSchedule`

```sql
CREATE TABLE [gse].[FlightSchedule] (
  [FlightID] INTEGER NOT NULL,
  [AirlineId] INTEGER,
  [AircraftId] INTEGER,
  [ArrivalFlight] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [FlightDate] DATE,
  [SeasonID] INTEGER,
  [FlightType] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Mission] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [DepartureFlight] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Origin] INTEGER,
  [Destination] INTEGER,
  [STA] DATETIME,
  [STD] DATETIME,
  [ATA] DATETIME,
  [ATD] DATETIME,
  [StandType] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [StandNumber] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TailNumber] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ContractAssigned] INTEGER,
  [TenantId] INTEGER,
  [Status] INTEGER,
  [ContractVerId] INTEGER,
  [SeasonVerId] INTEGER,
  [CreatedDate] DATETIME,
  [CreatedBy] INTEGER,
  [ContractFlightId] INTEGER,
  [TurnaroundTime] INTEGER
);
```
Sample Rows:
```text
FlightID	AirlineId	AircraftId	ArrivalFlight	FlightDate	SeasonID	FlightType	Mission	DepartureFlight	Origin	Destination	STA	STD	ATA	ATD	StandType	StandNumber	TailNumber	ContractAssigned	TenantId	Status	ContractVerId	SeasonVerId	CreatedDate	CreatedBy	ContractFlightId	TurnaroundTime
1	411	35	500	2025-09-20	None	Ad-Hoc	3	501	536	642	2025-09-19 16:00:00	2025-09-19 16:55:00	None	None	None	None	None	None	1	1	None	None	None	None	None	-55

```

### TABLE: `gse.FlightSeason`

```sql
CREATE TABLE [gse].[FlightSeason] (
  [SeasonID] INTEGER NOT NULL,
  [AirlineId] INTEGER,
  [AircraftId] INTEGER,
  [StandType] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Mission] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ArrivalFlight] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [DepartureFlight] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Origin] INTEGER,
  [Destination] INTEGER,
  [StartPeriod] DATETIME,
  [EndPeriod] DATETIME,
  [Sun] BIT,
  [Mon] BIT,
  [Tue] BIT,
  [Wed] BIT,
  [Thu] BIT,
  [Fri] BIT,
  [Sat] BIT,
  [ArrivalTime] DATETIME,
  [DepartureTime] DATETIME,
  [ContractID] INTEGER,
  [TenantId] INTEGER,
  [Status] INTEGER,
  [ContractVerId] INTEGER,
  [SeasonVerId] INTEGER,
  [CreatedDate] DATETIME,
  [CreatedBy] INTEGER,
  [ContractFlightId] INTEGER,
  [TurnaroundTime] INTEGER
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.FlightSeasonVersion`

```sql
CREATE TABLE [gse].[FlightSeasonVersion] (
  [SeasonVerId] INTEGER NOT NULL,
  [SeasonId] INTEGER NOT NULL,
  [VersionNo] INTEGER,
  [VersionDescription] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [CreatedDate] DATETIME,
  [CreatedBy] INTEGER
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.GeoFenceAlerts`

```sql
CREATE TABLE [gse].[GeoFenceAlerts] (
  [AlertID] INTEGER NOT NULL,
  [AlertName] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [LocationID] INTEGER,
  [GeoFenceType] NVARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [SpeedLimit] INTEGER,
  [FlightParked] BIT,
  [TimeBased] BIT,
  [LocationOfDevice] BIT,
  [AssetID] INTEGER,
  [StartTime] TIME,
  [EndTime] TIME,
  [DurationSecs] INTEGER,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
AlertID	AlertName	LocationID	GeoFenceType	SpeedLimit	FlightParked	TimeBased	LocationOfDevice	AssetID	StartTime	EndTime	DurationSecs	TenantId
1	Speeding 25 Kmph	None	SpeedLimit	25	None	True	None	None	10:00:00	20:00:00	None	6

```

### TABLE: `gse.GeoFenceAlertsGSE`

```sql
CREATE TABLE [gse].[GeoFenceAlertsGSE] (
  [AlertGSEID] INTEGER NOT NULL,
  [AlertID] INTEGER NOT NULL,
  [GSETypeID] INTEGER NOT NULL
);
```
Sample Rows:
```text
AlertGSEID	AlertID	GSETypeID
1	1	1700
2	1	1720

```

### TABLE: `gse.GeoFenceAlertsUser`

```sql
CREATE TABLE [gse].[GeoFenceAlertsUser] (
  [AlertUserID] INTEGER NOT NULL,
  [AlertID] INTEGER NOT NULL,
  [UserID] INTEGER NOT NULL
);
```
Sample Rows:
```text
AlertUserID	AlertID	UserID
1	1	7

```

### TABLE: `gse.GeoFenceLocation`

```sql
CREATE TABLE [gse].[GeoFenceLocation] (
  [AlertLocId] INTEGER NOT NULL,
  [AlertId] INTEGER NOT NULL,
  [LocationId] INTEGER NOT NULL
);
```
Sample Rows:
```text
AlertLocId	AlertId	LocationId
1	1	831
2	1	833

```

### TABLE: `gse.GraphData`

```sql
CREATE TABLE [gse].[GraphData] (
  [GraphId] INTEGER NOT NULL,
  [GraphName] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [xAxisLabel] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [yAxisLabel] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [xLabels] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [yData] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [BackgroundColor] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [GaugeValue] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [GaugeValueColor] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [GaugeLimits] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [CompanyId] INTEGER,
  [CompanyName] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [MessageOn] DATETIME,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.GSEAircraft`

```sql
CREATE TABLE [gse].[GSEAircraft] (
  [Id] INTEGER NOT NULL,
  [AircraftId] INTEGER,
  [GSEId] INTEGER
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.GSEAllocation`

```sql
CREATE TABLE [gse].[GSEAllocation] (
  [AllocationID] INTEGER NOT NULL,
  [FlightPlanID] INTEGER NOT NULL,
  [MissionID] INTEGER,
  [AssetID] INTEGER,
  [ExpStart] DATETIME,
  [ExpEnd] DATETIME,
  [ActualStart] DATETIME,
  [ActualEnd] DATETIME,
  [Status] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Remarks] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.GSEGroup`

```sql
CREATE TABLE [gse].[GSEGroup] (
  [GSEGroupId] INTEGER NOT NULL,
  [GroupName] NVARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [GSEId] INTEGER,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
GSEGroupId	GroupName	GSEId	TenantId
1	AIRSIDE	None	20
2	LANDSIDE	None	20
3	Turnaround	None	20

```

### TABLE: `gse.GSEGroupItem`

```sql
CREATE TABLE [gse].[GSEGroupItem] (
  [GroupItemId] INTEGER NOT NULL,
  [GroupId] INTEGER,
  [GSEId] INTEGER
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.GSEMaster`

```sql
CREATE TABLE [gse].[GSEMaster] (
  [GSEID] INTEGER NOT NULL,
  [AssetNo] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [AssetName] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [Description] NVARCHAR(400) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [SerialNo] NVARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Barcode] NVARCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [PassiveRFID] NVARCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ActiveRFID] NVARCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [BLE] NVARCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [CompanyID] INTEGER,
  [CategoryID] INTEGER NOT NULL,
  [LocationID] INTEGER,
  [CompanyName] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [CategoryName] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [LocationName] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ModelNo] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [Make] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [AssetStatus] BIT,
  [EquipmentType] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ResourceCode] INTEGER,
  [LastLat] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [LastLang] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [LastSeenTime] DATETIME,
  [LastSeenLocation] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [AssignedDeviceID] INTEGER,
  [Heading] INTEGER,
  [OwnerId] INTEGER,
  [TenantId] INTEGER NOT NULL,
  [YearInstalled] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [LicensePlate] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [LicenseExpiry] DATETIME,
  [InsuranceExpiry] DATETIME,
  [FuelCapacity] NVARCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [FuelEconomy] NVARCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [SpeedLimitKPH] NVARCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [DisplayName] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [IMEINumber] INTEGER,
  [Maint_EngHours] INTEGER,
  [Maint_Days] INTEGER,
  [Maint_Mileage] INTEGER,
  [EngineStatus] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [OperatingStatus] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [AuxiliaryStatus] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [DriverID] INTEGER,
  [LOP] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [HCT] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Battery] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [FuelLevel] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [CurrentSpeed] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Overspeeding] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Acceleration] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [BrakingEvents] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [MoveStatus] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [InMaintenance] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [InMaintenanceUnPlan] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [MV] FLOAT,
  [BV] FLOAT,
  [LastMaintOn] DATETIME,
  [Fuel0V] FLOAT,
  [Fuel100V] FLOAT,
  [isFuelEnabled] BIT,
  [isEngineSignal] BIT,
  [EngineCutoffVoltage] FLOAT,
  [NextMaintOn] DATETIME,
  [AssetDesign] INTEGER,
  [EnergySource] INTEGER,
  [FuelType] INTEGER,
  [AreaOfUse] INTEGER,
  [MaintenanceStrategy] INTEGER,
  [InstallationDate] DATETIME,
  [GoLiveDate] DATETIME,
  [DeviceWarrantyStartDate] DATETIME,
  [DeviceWarrantyEndDate] DATETIME,
  [SimCardProvider] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [SimAPN] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [DataPeriod] INTEGER,
  [SimCardRenewalDate] DATETIME,
  [DataPackageRenewalDate] DATETIME,
  [ACEnabled] BIT,
  [ACReaderSN] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ACWarrantyStartDate] DATETIME,
  [ACWarrantyEndDate] DATETIME,
  [OperatingDept] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [EngineCapacity] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [BatteryVoltage] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [YearOfMfg] DATETIME,
  [LeasedFrom] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [LeaseDuration] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [LeaseStartOn] DATETIME,
  [LeaseEndOn] DATETIME,
  [AVP] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [AVPExpiryDate] DATETIME,
  [AircraftId] INTEGER,
  [DeviceSerialNo] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [VinNo] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Maintenanceid] INTEGER,
  [InitialOdometer] INTEGER,
  [OdometerDate] DATETIME,
  [CurrentOdometer] INTEGER,
  [InitialEngineHours] FLOAT,
  [EngineHoursDate] DATETIME,
  [CurrentEngineHours] FLOAT,
  [isnme] BIT,
  [Occupancy] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [OccupancyValue] INTEGER,
  [BatteryStatus] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [flightno] NVARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [uld_palletno] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [tractorid] INTEGER,
  [StationId] INTEGER,
  [LastStatusChange] DATETIME,
  [MaintCreatedBy] INTEGER,
  [MaintCreatedOn] DATETIME,
  [ZoneID] INTEGER,
  [FWDMove] BIT,
  [BCKMove] BIT,
  [HNDBrake] BIT,
  [HYDFunc] BIT,
  [STRFunc] BIT,
  [TractionHrs] INTEGER,
  [HydralicHrs] INTEGER,
  [PermitTypeId] INTEGER,
  [PermitStartDate] DATETIME,
  [InspectionRenewal] BIT,
  [PermitNotes] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [FaultCode] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [FaultLevel] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [BatteryTemp] INTEGER,
  [SoH] INTEGER,
  [BatteryCurr] INTEGER,
  [TractionHrsOffset] INTEGER,
  [HydralicHrsOffset] INTEGER,
  [OpStartTime] DATETIME,
  [DriverName] VARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [DynamicData] VARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS"
);
```
Sample Rows:
```text
GSEID	AssetNo	AssetName	Description	SerialNo	Barcode	PassiveRFID	ActiveRFID	BLE	CompanyID	CategoryID	LocationID	CompanyName	CategoryName	LocationName	ModelNo	Make	AssetStatus	EquipmentType	ResourceCode	LastLat	LastLang	LastSeenTime	LastSeenLocation	AssignedDeviceID	Heading	OwnerId	TenantId	YearInstalled	LicensePlate	LicenseExpiry	InsuranceExpiry	FuelCapacity	FuelEconomy	SpeedLimitKPH	DisplayName	IMEINumber	Maint_EngHours	Maint_Days	Maint_Mileage	EngineStatus	OperatingStatus	AuxiliaryStatus	DriverID	LOP	HCT	Battery	FuelLevel	CurrentSpeed	Overspeeding	Acceleration	BrakingEvents	MoveStatus	InMaintenance	InMaintenanceUnPlan	MV	BV	LastMaintOn	Fuel0V	Fuel100V	isFuelEnabled	isEngineSignal	EngineCutoffVoltage	NextMaintOn	AssetDesign	EnergySource	FuelType	AreaOfUse	MaintenanceStrategy	InstallationDate	GoLiveDate	DeviceWarrantyStartDate	DeviceWarrantyEndDate	SimCardProvider	SimAPN	DataPeriod	SimCardRenewalDate	DataPackageRenewalDate	ACEnabled	ACReaderSN	ACWarrantyStartDate	ACWarrantyEndDate	OperatingDept	EngineCapacity	BatteryVoltage	YearOfMfg	LeasedFrom	LeaseDuration	LeaseStartOn	LeaseEndOn	AVP	AVPExpiryDate	AircraftId	DeviceSerialNo	VinNo	Maintenanceid	InitialOdometer	OdometerDate	CurrentOdometer	InitialEngineHours	EngineHoursDate	CurrentEngineHours	isnme	Occupancy	OccupancyValue	BatteryStatus	flightno	uld_palletno	tractorid	StationId	LastStatusChange	MaintCreatedBy	MaintCreatedOn	ZoneID	FWDMove	BCKMove	HNDBrake	HYDFunc	STRFunc	TractionHrs	HydralicHrs	PermitTypeId	PermitStartDate	InspectionRenewal	PermitNotes	FaultCode	FaultLevel	BatteryTemp	SoH	BatteryCurr	TractionHrsOffset	HydralicHrsOffset	OpStartTime	DriverName	DynamicData
6	N4	N4	None	None	None	None	None	None	1	495	823	None	None	None	155	156	True	FMV	2494	18.3049751	-15.9610839	2024-11-30 13:36:54.577000		None	352	None	15	2023	20022	None	None	50	0	50	N4	470	5000	90	500	OFF	AVAILABLE	UNKNOWN	0	False	False	False	0	0	False	False	False	OFF	Off	Off	12.7	10.0	2023-04-20 00:00:00	1.0	0.0	False	None	0.0	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	40716	None	None	None	False	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None
7	LDL001-NEW	LDL001-NEW	None	None	None	None	None	None	1	495	823	None	None	None	155	156	True	FMV	2494	18.3082884	-15.9638394	2024-05-06 17:14:47.280000		None	219	None	15	2022	20022	None	None	50	0	50	LDL001-NEW	459	5000	90	500	ON_NVA	STANDBY	UNKNOWN	0	False	False	False	0	0	False	False	False	OFF	Off	Off	28.1	0.0	2023-01-31 00:00:00	1.0	0.0	False	False	0.0	2023-05-01 00:00:00	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	False	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None
8	152STP012	152STP012	Pax Step	None	None	None	None	None	1	483	823	None	None	None	155	156	True	STP	2486	18.3051612	-15.9611939	2024-01-04 10:35:34.323000		None	51	None	15	2022	20022	None	None	50	0	50	152STP012	477	5000	90	500	OFF	AVAILABLE	UNKNOWN	0	False	False	False	0	0	False	False	False	OFF	Off	Off	0.0	0.0	2023-02-01 00:00:00	1.0	0.0	True	False	0.0	2023-05-02 02:24:00	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	False	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None	None

```

### TABLE: `gse.IdleTiming`

```sql
CREATE TABLE [gse].[IdleTiming] (
  [ID] INTEGER NOT NULL,
  [IdlingTimeInSec] INTEGER,
  [IDType] INTEGER,
  [GSEID] INTEGER
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.InactiveUnits`

```sql
CREATE TABLE [gse].[InactiveUnits] (
  [InactiveUnitsId] INTEGER NOT NULL,
  [VehicleID] INTEGER NOT NULL,
  [VehicleName] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [DeviceID] INTEGER NOT NULL,
  [DeviceName] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [LastMessageOn] DATETIME,
  [LastPositionLocation] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [DaysSince] INTEGER,
  [GSEType] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.IncidentReports`

```sql
CREATE TABLE [gse].[IncidentReports] (
  [IncidentReportId] INTEGER NOT NULL,
  [VehicleID] INTEGER NOT NULL,
  [AssetID] INTEGER NOT NULL,
  [IncidentStatus] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [IncidentNotes] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [GSEType] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [MessageOn] DATETIME,
  [TenantId] INTEGER NOT NULL,
  [IncidentType] INTEGER,
  [CreatedBy] INTEGER,
  [CreatedOn] DATETIME
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.IndoorMap`

```sql
CREATE TABLE [gse].[IndoorMap] (
  [ImageId] INTEGER NOT NULL,
  [TenantId] INTEGER NOT NULL,
  [ImageName] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ImageFile] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [LeftTop] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [LeftBottom] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [RightTop] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [RightBottom] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [CreatedBy] INTEGER,
  [CreatedOn] DATETIME
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.MaintenanceHistory`

```sql
CREATE TABLE [gse].[MaintenanceHistory] (
  [HistoryID] INTEGER NOT NULL,
  [GSEID] INTEGER NOT NULL,
  [MaintenanceTypeID] INTEGER NOT NULL,
  [MaintenanceDate] DATE NOT NULL,
  [UsageAtMaintenance] INTEGER,
  [Comments] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [tenantid] INTEGER,
  [ScheduleId] INTEGER,
  [Enteredby] INTEGER
);
```
Sample Rows:
```text
HistoryID	GSEID	MaintenanceTypeID	MaintenanceDate	UsageAtMaintenance	Comments	tenantid	ScheduleId	Enteredby
1	2221	1	2025-01-16	670	None	45	1	1
2	2292	1	2025-04-03	1616	None	45	7	69
3	2291	1	2025-04-03	977	None	45	4	69

```

### TABLE: `gse.MaintenanceNext`

```sql
CREATE TABLE [gse].[MaintenanceNext] (
  [MaintenanceId] INTEGER NOT NULL,
  [NextPMOn] DATETIME,
  [Comments] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [EnteredBy] INTEGER,
  [EnteredOn] DATETIME,
  [AssetId] INTEGER,
  [TenantId] INTEGER
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.MaintenanceSchedule`

```sql
CREATE TABLE [gse].[MaintenanceSchedule] (
  [ScheduleID] INTEGER NOT NULL,
  [GSEID] INTEGER NOT NULL,
  [MaintenanceTypeID] INTEGER NOT NULL,
  [NextDueDate] DATETIME,
  [NextDueUsage] INTEGER,
  [PendingCapacity] INTEGER,
  [LastUsage] INTEGER,
  [LastMaintenanceDate] DATETIME,
  [tenantid] INTEGER,
  [UsageThreshold] INTEGER,
  [Enteredby] INTEGER,
  [Status] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [CurrentReading] INTEGER,
  [InitialReading] INTEGER
);
```
Sample Rows:
```text
ScheduleID	GSEID	MaintenanceTypeID	NextDueDate	NextDueUsage	PendingCapacity	LastUsage	LastMaintenanceDate	tenantid	UsageThreshold	Enteredby	Status	CurrentReading	InitialReading
1	2221	1	2025-08-01 01:29:52.673000	3082	0	12831	2025-09-10 11:31:10.057000	45	1000	69		3886	0
2	2221	2	2026-09-10 11:31:10.300000	5753	1951	3753	2025-09-10 11:31:10.300000	45	2000	69		678	0
3	2221	3	2026-09-10 11:31:10.530000	8099	1893	6099	2025-09-10 11:31:10.530000	45	2000	69		1554	0

```

### TABLE: `gse.MaintenanceTypes`

```sql
CREATE TABLE [gse].[MaintenanceTypes] (
  [MaintenanceTypeID] INTEGER NOT NULL,
  [Name] NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [Description] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [IsScheduleBased] BIT,
  [IntervalDays] INTEGER,
  [UsageMetricTypeID] INTEGER,
  [UsageThreshold] INTEGER,
  [tenantid] INTEGER
);
```
Sample Rows:
```text
MaintenanceTypeID	Name	Description	IsScheduleBased	IntervalDays	UsageMetricTypeID	UsageThreshold	tenantid
1	Hour Meter (HMR)	Service based on hour meter	False	180	1	1000	45
2	Traction Motor - Hours	Traction system maintenance	False	365	2	2000	45
3	Hydraulic Motor - Hours	Hydraulic system maintenance	False	365	3	2000	45

```

### TABLE: `gse.MetricTypes`

```sql
CREATE TABLE [gse].[MetricTypes] (
  [MetricTypeID] INTEGER NOT NULL,
  [MetricName] NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [Description] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [tenantid] INTEGER
);
```
Sample Rows:
```text
MetricTypeID	MetricName	Description	tenantid
1	EngineHours	EngineHours	45
2	Traction	Traction	45
3	Hydraulic	Hydraulic	45

```

### TABLE: `gse.NMEGroup`

```sql
CREATE TABLE [gse].[NMEGroup] (
  [GroupId] INTEGER NOT NULL,
  [TractorId] INTEGER NOT NULL,
  [FlightNo] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [FlightDate] DATETIME,
  [Remarks] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [CreatedOn] DATETIME,
  [CreatedBy] INTEGER,
  [TenantId] INTEGER,
  [Status] BIT
);
```
Sample Rows:
```text
GroupId	TractorId	FlightNo	FlightDate	Remarks	CreatedOn	CreatedBy	TenantId	Status
1	3077	None	None	None	2024-04-17 00:00:00	42	41	True

```

### TABLE: `gse.NMEGroupDetails`

```sql
CREATE TABLE [gse].[NMEGroupDetails] (
  [GSEGroupId] INTEGER NOT NULL,
  [GSEId] INTEGER NOT NULL,
  [GroupId] INTEGER NOT NULL,
  [ULDNo] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Status] BIT,
  [TenantId] INTEGER
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.NMEGroupHistory`

```sql
CREATE TABLE [gse].[NMEGroupHistory] (
  [GroupHistoryId] INTEGER NOT NULL,
  [GroupId] INTEGER NOT NULL,
  [GSEId] INTEGER,
  [ULDNo] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Status] BIT,
  [CreatedOn] DATETIME,
  [CreatedBy] INTEGER,
  [TenantId] INTEGER,
  [TractorId] INTEGER,
  [FlightNo] NVARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [FlightDate] DATETIME
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.NotificationRules`

```sql
CREATE TABLE [gse].[NotificationRules] (
  [RuleId] INTEGER NOT NULL,
  [RuleName] NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [EventTypeId] INTEGER NOT NULL,
  [EmailMsg] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [SMSMsg] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ThresholdValue] FLOAT,
  [GeofenceAlertId] INTEGER,
  [NotifyOnEmail] BIT,
  [NotifyOnSMS] BIT,
  [NotifyOnWhatsApp] BIT,
  [NotifyOnPushNotify] BIT,
  [SendFrequency] INTEGER,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.NotificationRulesUser`

```sql
CREATE TABLE [gse].[NotificationRulesUser] (
  [NotificationUserID] INTEGER NOT NULL,
  [RuleId] INTEGER NOT NULL,
  [UserID] INTEGER NOT NULL
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.NotificationRulesUserGroup`

```sql
CREATE TABLE [gse].[NotificationRulesUserGroup] (
  [NotificationUserGroupId] INTEGER NOT NULL,
  [RuleId] INTEGER NOT NULL,
  [UserGroupId] INTEGER NOT NULL
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.PeakUtilization`

```sql
CREATE TABLE [gse].[PeakUtilization] (
  [AutoID] INTEGER NOT NULL,
  [GSETypeID] INTEGER,
  [GSETypeName] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TimeSlot] DATETIME,
  [Count] INTEGER,
  [TenantId] INTEGER
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.POIMaster`

```sql
CREATE TABLE [gse].[POIMaster] (
  [POIId] INTEGER NOT NULL,
  [Description] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Icon] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Latitude] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Longitude] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantId] INTEGER NOT NULL,
  [TagId] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS"
);
```
Sample Rows:
```text
POIId	Description	Icon	Latitude	Longitude	TenantId	TagId
77	Test POI	ASSET	24.952311149513548	46.6885149788213	20	NA
78	TrackIT Office	OFFICE	25.123422	55.4249441	42	F98C734A2806

```

### TABLE: `gse.ProcessedFile`

```sql
CREATE TABLE [gse].[ProcessedFile] (
  [FullName] VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [Lines] INTEGER
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.PushNotify`

```sql
CREATE TABLE [gse].[PushNotify] (
  [PushNotifyId] INTEGER NOT NULL,
  [GseId] INTEGER,
  [VehicleId] INTEGER,
  [Owner] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [NotifyOn] DATETIME,
  [TenantId] INTEGER,
  [DeviceName] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [IconName] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [NotifyText] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [EventTypeID] INTEGER
);
```
Sample Rows:
```text
PushNotifyId	GseId	VehicleId	Owner	NotifyOn	TenantId	DeviceName	IconName	NotifyText	EventTypeID
1	181	181	Oxagon - 35	2024-03-30 14:46:19	39	7291-RRB	OverSpeedingOn.png	7291-RRB OverSpeedingOn - 42 kmp/h Limit:25 km/h at Ramp Area SAL Cargo	34
2	188	188	Oxagon - 35	2024-03-30 14:26:19	39	7884-UBB	OverSpeedingOn.png	7884-UBB OverSpeedingOn - 42 kmp/h Limit:25 km/h at Ramp Area SAL Cargo	34
3	189	189	Oxagon - 35	2024-03-30 13:16:19	39	6798-XBB	OverSpeedingOn.png	6798-XBB OverSpeedingOn - 42 kmp/h Limit:25 km/h at Ramp Area SAL Cargo	34

```

### TABLE: `gse.ReferenceLoc`

```sql
CREATE TABLE [gse].[ReferenceLoc] (
  [ID] INTEGER NOT NULL,
  [MacAddress] VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Latitude] VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Longitude] VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [geom] NULL
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.ReportType`

```sql
CREATE TABLE [gse].[ReportType] (
  [ReportID] INTEGER NOT NULL,
  [ReportName] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS"
);
```
Sample Rows:
```text
ReportID	ReportName
0	GetCurrentPos
1	DownloadLog
2	Location

```

### TABLE: `gse.ServiceTypes`

```sql
CREATE TABLE [gse].[ServiceTypes] (
  [ServiceId] INTEGER NOT NULL,
  [ServiceType] INTEGER NOT NULL,
  [ServiceName] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [IconImage] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
ServiceId	ServiceType	ServiceName	IconImage	TenantId
1	1	In Service	ServiceIcon/00000/00000001_sxwhobqasz2tw.png	42
2	3	Planned Inspection	ServiceIcon/00000/00000002_khsmodgbmrv2y.png	42
3	4	Unplanned Inspection	ServiceIcon/00000/00000003_5m3zuyudezddm.png	42

```

### TABLE: `gse.StationMaster`

```sql
CREATE TABLE [gse].[StationMaster] (
  [StationId] INTEGER NOT NULL,
  [StationCountry] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [StationCity] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [StationCode] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [StationName] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantId] INTEGER NOT NULL,
  [geom] NULL,
  [GeofenceOpacity] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [geocolor] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [geoborderColor] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS"
);
```
Sample Rows:
```text
StationId	StationCountry	StationCity	StationCode	StationName	TenantId	geom	GeofenceOpacity	geocolor	geoborderColor
1	India	Bangalore	BLR	Bangalore International Airport	41	None	None	None	None
2	India	Amritsar	ATQ	ATQ	43	None	None	None	None
3	Columbia	Bogota	BOG	Bogota	44	None	None	None	None

```

### TABLE: `gse.SystemLogs`

```sql
CREATE TABLE [gse].[SystemLogs] (
  [ID] INTEGER NOT NULL,
  [EventDate] DATETIME NOT NULL,
  [LogLevel] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [LogMessage] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Exception] NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [SourceType] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [UserId] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ZoneInfoId] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ModuleId] NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.SystemSettings`

```sql
CREATE TABLE [gse].[SystemSettings] (
  [ID] INTEGER NOT NULL,
  [Name] NVARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL
);
```
Sample Rows:
```text
ID	Name
1	Latitude
2	Longitude
3	No Of Stations

```

### TABLE: `gse.TelegramUsers`

```sql
CREATE TABLE [gse].[TelegramUsers] (
  [ChatID] VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [FirstName] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [LastName] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [UserID] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [CreatedOn] DATETIME
);
```
Sample Rows:
```text
ChatID	FirstName	LastName	UserID	CreatedOn
112217812	Wanlun	Wanlun	w	2020-11-06 02:58:52.130000
1360505992	Husain	Ragib	hbragib	2020-11-03 16:13:16.227000
1412772813	Vijai	Nair	vijainair	2020-11-03 16:13:16.237000

```

### TABLE: `gse.TurnaroundCAG`

```sql
CREATE TABLE [gse].[TurnaroundCAG] (
  [TurnaroundID] INTEGER NOT NULL,
  [AircraftType] NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [StandType] NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Gate] NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [OperationType] NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ETA_ATA] DATETIME,
  [ETD_ATD] DATETIME,
  [STP] NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [LDL] NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [MDL] NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [MCB] NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TTR] NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ACU] NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [GPU] NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [WSU] NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TSU] NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [PBT] NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.TurnaroundMaster`

```sql
CREATE TABLE [gse].[TurnaroundMaster] (
  [TurnaroundID] INTEGER NOT NULL,
  [FlightId] INTEGER,
  [FlightNo] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [AircraftType] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Gate] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [FlightType] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ETA] DATETIME,
  [ETD] DATETIME,
  [AssetType] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [AssetTypeVal] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [AvailableCount] INTEGER,
  [RequiredCount] INTEGER,
  [StartTime] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [EndTime] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantId] INTEGER NOT NULL,
  [CreatedBy] INTEGER,
  [CreatedOn] DATETIME,
  [Status] INTEGER,
  [AssetTypeOrderBy] INTEGER
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.TurnaroundMon`

```sql
CREATE TABLE [gse].[TurnaroundMon] (
  [TurnaroundID] INTEGER NOT NULL,
  [FlightNo] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [AircraftType] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Gate] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [FlightType] NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ETA] DATETIME,
  [ETD] DATETIME,
  [STP] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [LDL] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [MCB] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TTR] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [ACU] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [GPU] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [WSU] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TSU] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [PBT] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [MDL] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [PBUS] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TPT] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TBL] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [BC] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [LD3] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [10F] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TOW] NVARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
TurnaroundID	FlightNo	AircraftType	Gate	FlightType	ETA	ETD	STP	LDL	MCB	TTR	ACU	GPU	WSU	TSU	PBT	MDL	PBUS	TPT	TBL	BC	LD3	10F	TOW	TenantId
1	L6128
	B737
	A22	DEP	None	2020-09-11 15:30:00	2/2,14:55 - 14:55
	None	2/2,14:50 - 14:50	2/3,14:55 - 15:25	1/1,15:05 - 15:28	1/1,15:05 - 15:28	None	None	1/1,15:25	None	None	None	None	None	None	None	None	1
2	L6128
	A321
	A10	DEP	None	2020-09-11 17:00:00	1/1,16:25 - 16:58
	None	1/2,16:20 - 16:58
	3/3,16:25 - 16:55	None	None	None	None	1/1,16:55	None	None	None	None	None	None	None	None	1
3	TK595
	B737
	C16	T/A	2020-09-11 17:40:00	2020-09-11 18:25:00	0/1,17:38 - 18:23
	None	0/2,17:38 - 18:23	3/3,17:42 - 18:23	None	None	1/1,17:55 - 18:00
	1/1,18:00 - 18:05	1/1,18:20	None	None	None	None	None	None	None	None	1

```

### TABLE: `gse.UserGroup`

```sql
CREATE TABLE [gse].[UserGroup] (
  [UserGroupId] INTEGER NOT NULL,
  [GroupName] NVARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [UserId] INTEGER,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.UserGroupItem`

```sql
CREATE TABLE [gse].[UserGroupItem] (
  [UserGroupItemId] INTEGER NOT NULL,
  [UserGroupId] INTEGER,
  [UserId] INTEGER
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.VehicleAssessment`

```sql
CREATE TABLE [gse].[VehicleAssessment] (
  [VehicleAssessmentId] INTEGER NOT NULL,
  [VehicleID] INTEGER NOT NULL,
  [VehicleName] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" NOT NULL,
  [Rank] DECIMAL(5, 2),
  [Penalty] INTEGER,
  [Violations] INTEGER,
  [Duration] NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [Mileage] DECIMAL(20, 2),
  [Trips] INTEGER,
  [MessageOn] DATETIME,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.VehicleMaintenance`

```sql
CREATE TABLE [gse].[VehicleMaintenance] (
  [Id] INTEGER NOT NULL,
  [MaintenanceId] INTEGER,
  [AssetId] INTEGER,
  [LastTriggerOn] DATETIME,
  [LastTriggerAt] INTEGER,
  [isCompleted] BIT,
  [CompletedOn] DATETIME,
  [CompletedBy] INTEGER,
  [Remarks] VARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS"
);
```
Sample Rows:
```text
No rows.
```

### TABLE: `gse.VehicleMovement`

```sql
CREATE TABLE [gse].[VehicleMovement] (
  [AssetMovementID] INTEGER NOT NULL,
  [AssetNo] NVARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [LocationName] NVARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS",
  [StartTime] DATETIME,
  [EndTime] DATETIME,
  [Duration] TIME,
  [TenantId] INTEGER NOT NULL
);
```
Sample Rows:
```text
No rows.
```


## 👁️ SELECTED VIEWS

### VIEW: `gse.vwGSEAssets`

Columns:

| Column | Type | Nullable |
|--------|------|----------|
| isnme | BIT | YES |
| TenantId | INTEGER | NO |
| AssetID | INTEGER | NO |
| AssetNo | NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | NO |
| AssetName | NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" | NO |
| AllocatedToFlight | NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| Description | NVARCHAR(400) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| BLE | NVARCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| CompanyID | INTEGER | YES |
| CategoryID | INTEGER | NO |
| LocationID | INTEGER | YES |
| CompanyName | NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| CategoryName | NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| LocationName | NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| ModelNo | NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | NO |
| Make | NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" | NO |
| ResourceCode | INTEGER | YES |
| LastLat | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | NO |
| LastLang | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | NO |
| LastSeenTime | DATETIME | NO |
| LastSeenLocationId | INTEGER | NO |
| LastSeenLocation | NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | NO |
| AssignedDeviceID | INTEGER | YES |
| EquipmentType | NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| EquipmentTypeName | NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| LocName | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| VehicleID | INTEGER | NO |
| DisplayName | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| Maint_EngHours | INTEGER | YES |
| Maint_Days | INTEGER | YES |
| Maint_Mileage | INTEGER | NO |
| EngineStatus | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| OperatingStatus | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| AuxiliaryStatus | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| LOP | NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| HCT | NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| Battery | NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| FuelLevel | NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| CurrentSpeed | NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| Overspeeding | NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| Acceleration | NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| BrakingEvents | NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| FuelCapacity | NVARCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| SpeedLimitKPH | NVARCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | NO |
| IMEINumber | NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | NO |
| Heading | INTEGER | YES |
| DeviceID | INTEGER | NO |
| ModelNumber | NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | NO |
| EquipmentTypeID | INTEGER | NO |
| HeadingOffset | INTEGER | YES |
| DeviceTypeID | INTEGER | NO |
| OwnerCode | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | NO |
| MV | FLOAT | YES |
| BV | FLOAT | YES |
| GeoFenceType | NVARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| InMaintenance | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| Fuel0V | FLOAT | YES |
| Fuel100V | FLOAT | YES |
| isFuelEnabled | BIT | YES |
| EngineCutoffVoltage | FLOAT | YES |
| IsEngineSignal | BIT | YES |
| IsHCT | BIT | YES |
| IsLOP | BIT | YES |
| IsWork | BIT | YES |
| EnginePort | INTEGER | YES |
| HCTPort | INTEGER | YES |
| LOPPort | INTEGER | YES |
| Work1Port | INTEGER | YES |
| Work2Port | INTEGER | YES |
| Work3Port | INTEGER | YES |
| Work4Port | INTEGER | YES |
| Work1Name | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| Work2Name | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| Work3Name | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| Work4Name | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| DriverName1 | NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" | NO |
| DriverID | INTEGER | YES |
| InMaintenanceUnPlan | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| LastMaintOn | DATETIME | YES |
| NextMaintOn | DATETIME | YES |
| MaintenanceType | INTEGER | YES |
| MaintenanceStatus | NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" | NO |
| CurrentOdometer | INTEGER | YES |
| CurrentEngineHours | FLOAT | YES |
| DeviceType | NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| FuelType | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| FuelPort | INTEGER | YES |
| TimeZoneId | INTEGER | YES |
| LowVoltage | FLOAT | YES |
| UnderVoltage | FLOAT | YES |
| OverVoltage | FLOAT | YES |
| FuelSlope | FLOAT | YES |
| FuelOffset | FLOAT | YES |
| OwnerId | INTEGER | YES |
| YearOfMfg | DATETIME | YES |
| InstallationDate | DATETIME | YES |
| EngineCapacity | DECIMAL(18, 2) | YES |
| Occupancy | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| OccupancyValue | INTEGER | YES |
| BatteryStatus | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| NMEFlightNo | NVARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| uld_palletno | NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| tractorid | INTEGER | YES |
| TractorNo | NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| NmeLastLat | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| NmeLastLang | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| StationId | INTEGER | YES |
| StationCode | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| Expr1 | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| OwnerName | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| MaintCreatedBy | NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| MaintCreatedOn | DATETIME | YES |
| TimeZoneValue | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| MaintStrategy | NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| EngineHoursDate | DATETIME | YES |
| InitialEngineHours | FLOAT | YES |
| ExceptionNotes | NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| FWDMove | BIT | YES |
| BCKMove | BIT | YES |
| HNDBrake | BIT | YES |
| HYDFunc | BIT | YES |
| STRFunc | BIT | YES |
| mapid | INTEGER | NO |
| xCoordinate | INTEGER | NO |
| yCoordinate | INTEGER | NO |
| TractionHrs | INTEGER | YES |
| HydralicHrs | INTEGER | YES |
| AVP | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| AVPExpiryDate | DATETIME | YES |
| BatteryCurr | INTEGER | YES |
| BatteryTemp | INTEGER | YES |
| SoH | INTEGER | YES |
| MapIconColor | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| OpStartTime | DATETIME | YES |
| TenantKey | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| TenantEmail | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| newIconName | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | NO |
| DriverName | VARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| DynamicData | VARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |

DDL:
```sql
-- View definition not available
```

### VIEW: `gse.vwGSEStatus`

Columns:

| Column | Type | Nullable |
|--------|------|----------|
| ISNME | BIT | YES |
| TenantId | INTEGER | NO |
| GSEID | INTEGER | NO |
| GSE | NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | NO |
| GSEType | NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| GSETypeName | NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| EquipmentTypeID | INTEGER | NO |
| DriverID | INTEGER | YES |
| OperatorName | VARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| AllocatedToFlight | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" | NO |
| EngineStatus | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| OperatingStatus | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| LOP | NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| HCT | NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| Battery | NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| MV | FLOAT | YES |
| BV | FLOAT | YES |
| OwnerCode | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | NO |
| GeoFenceType | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" | NO |
| FuelLevel | VARCHAR(4) COLLATE "SQL_Latin1_General_CP1_CI_AS" | NO |
| Fuel | NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| CurrentSpeed | NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| Overspeeding | NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| Acceleration | NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| BrakingEvents | NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| InMaintenance | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| InMaintenanceUnPlan | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| LastSeenTime | DATETIME | NO |
| LocationID | INTEGER | YES |
| LastSeenLocationId | INTEGER | NO |
| LastSeenLocation | NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | NO |
| NextMaintOn | DATETIME | YES |
| LastMaintOn | DATETIME | YES |
| MaintenanceType | INTEGER | YES |
| MaintenanceStatus | NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" | NO |
| CurrentOdometer | INTEGER | YES |
| CurrentEngineHours | FLOAT | YES |
| OwnerId | INTEGER | YES |
| EngineCapacity | DECIMAL(18, 2) | YES |
| occupancy | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| occupancyvalue | INTEGER | YES |
| batterystatus | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| NMEFlightNo | NVARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| uld_palletno | NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| Tractorid | INTEGER | YES |
| TractorNo | NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| StationId | INTEGER | YES |
| StationCode | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| MaintCreatedBy | NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| MaintCreatedOn | DATETIME | YES |
| ExceptionNotes | NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| TractionHrs | INTEGER | YES |
| HydralicHrs | INTEGER | YES |
| AVP | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| AVPExpiryDate | DATETIME | YES |
| BatteryCurr | INTEGER | YES |
| BatteryTemp | INTEGER | YES |
| SoH | INTEGER | YES |
| Online/Offline | VARCHAR(7) COLLATE "SQL_Latin1_General_CP1_CI_AS" | NO |
| RequiresAttention | INTEGER | NO |
| ServiceIcon | NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| newIconName | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | NO |
| DriverName | VARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| DynamicData | VARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS" | YES |
| RowID | BIGINT | YES |

DDL:
```sql
-- View definition not available
```
