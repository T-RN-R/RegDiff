

ACE_TYPES = {
    "A": "ACCESS_ALLOWED",
    "D": "ACCESS_DENIED",
    "OA": "ACCESS_ALLOWED_OBJECT",
    "OD": "ACCESS_DENIED_OBJECT",
    "AU": "SYSTEM_AUDIT",
    "AL": "SYSTEM_ALARM",
    "OU": "SYSTEM_AUDIT_OBJECT",
    "OL": "SYSTEM_ALARM_OBJECT"
}

ACE_FLAGS = {
    "CI": "CONTAINER_INHERIT",
    "OI": "OBJECT_INHERIT",
    "NP": "NO_PROPAGATE_INHERIT",
    "IO": "INHERIT_ONLY",
    "ID": "INHERITED",
    "SA": "SUCCESSFUL_ACCESS",
    "FA": "FAILED_ACCESS"
}

GENERIC_PERMISSIONS = {
    "GA": "GENERIC_ALL",
    "GX": "GENERIC_EXECUTE",
    "GW": "GENERIC_WRITE",
    "GR": "GENERIC_READ",

    "SD": "DELETE",
    "RC": "READ_CONTROL",
    "WD": "WRITE_DAC",
    "WO": "WRITE_OWNER"
}

PERMISSIONS_FILE = {
    "CC": "READ",
    "DC": "WRITE",
    "LC": "APPEND",
    "SW": "READ_EXTENDED_ATTRIBUTES",
    "RP": "WRITE_EXTENDED_ATTRIBUTES",
    "WP": "EXECUTE",
    "DT": "MEANINGLESS",
    "LO": "READ_ATTRIBUTES",
    "CR": "WRITE_ATTRIBUTES"
}

PERMISSIONS_DIRECTORY = {
    "CC": "LIST",
    "DC": "ADD_FILE",
    "LC": "ADD_SUB_DIR",
    "SW": "READ_EXTENDED_ATTRIBUTES",
    "RP": "WRITE_EXTENDED_ATTRIBUTES",
    "WP": "TRAVERSE",
    "DT": "DELETE_CHILD",
    "LO": "READ_ATTRIBUTES",
    "CR": "WRITE_ATTRIBUTES"
}

PERMISSIONS_FILE_MAP = {
    "CC": "FILE_MAP_COPY",
    "DC": "FILE_MAP_WRITE",
    "LC": "FILE_MAP_READ",
    "SW": "FILE_MAP_EXECUTE",
    "RP": "FILE_MAP_EXTEND_MAX_SIZE",
    "WP": "SECTION_MAP_EXECUTE_EXPLICIT"
}

PERMISSIONS_REGISTRY = {
    "CC": "QUERY",
    "DC": "SET",
    "LC": "CREATE_SUB_KEY",
    "SW": "ENUM_SUB_KEY",
    "RP": "NOTIFY",
    "WP": "CREATE_LINK"
}

PERMISSIONS_SERVICE_CONTROL = {
    "CC": "CONNECT",
    "DC": "CREATE_SERVICE",
    "LC": "ENUM_SERVICE",
    "SW": "LOCK",
    "RP": "QUERY_LOCK",
    "WP": "MODIFY_BOOT_CFG"
}

PERMISSIONS_SERVICE = {
    "CC": "QUERY_CONFIG",
    "DC": "CHANGE_CONFIG",
    "LC": "QUERY_STATISTIC",
    "SW": "ENUM_DEPENDENCIES",
    "RP": "START",
    "WP": "STOP",
    "DT": "PAUSE",
    "LO": "INTERROGATE",
    "CR": "USER_DEFINIED"
}

PERMISSIONS_PROCESS = {
    "CC": "TERMINATE",
    "DC": "CREATE_THREAD",
    "LC": "SET",
    "SW": "VM_OPERATE",
    "RP": "VM_READ",
    "WP": "VM_WRITE",
    "DT": "DUP_HANDLE",
    "LO": "CREATE_PROCESS",
    "CR": "SET_QUOTA"
}

PERMISSIONS_THREAD = {
    "CC": "TERMINATE",
    "DC": "SUSPEND",
    "LC": "ALERT",
    "SW": "GET_CONTEXT",
    "RP": "SET_CONTEXT",
    "WP": "SET_INFO",
    "DT": "QUERY_INFO",
    "LO": "SET_TOKEN",
    "CR": "IMPERSONATE"
}

PERMISSIONS_WINDOW_STATION = {
    "CC": "ENUM_DESKTOPS",
    "DC": "READ_ATTRIBUTE",
    "LC": "CLIPBOARD",
    "SW": "CREATE_DESKTOP",
    "RP": "WRITE_ATTRIBUTE",
    "WP": "GLOBAL_ATOMS",
    "DT": "EXIT_WINDOWS",
    "LO": "",
    "CR": "ENUM_WINSTA"
}

PERMISSIONS_DESKTOP = {
    "CC": "READ_OBJECTS",
    "DC": "CREATE_WINDOW",
    "LC": "CREATE_MENU",
    "SW": "HOOK_CONTROL",
    "RP": "JOURNAL_RECORD",
    "WP": "JOURNAL_PLAYBACK",
    "DT": "ENUM",
    "LO": "WRITE_OBJECTS",
    "CR": "SWITCH_DESKTOP"
}

PERMISSIONS_PIPE = {
    "CC": "READ",
    "DC": "WRITE",
    "LC": "CREATE_INSTANCE",
    "SW": "READ_EXTENDED_ATTRIBUTES",
    "RP": "WRITE_EXTENDEN_ATTRIBUTES",
    "WP": "EXECUTE",
    "DT": "DELETE",
    "LO": "READ_ATTRIBUTES",
    "CR": "WRITE_ATTRIBUTES"
}

PERMISSIONS_TOKEN = {
    "CC": "ASSIGN_PRIMARY",
    "DC": "DUPLICATE",
    "LC": "IMPERSONATE",
    "SW": "QUERY",
    "RP": "QUERY_SOURCE",
    "WP": "ADJUST_PRIVELEGES",
    "DT": "ADJUST_GROUPS",
    "LO": "ADJUST_DEFAULT",
    "CR": "ADJUST_SESSION"
}

GROUPED_PERMISSIONS = {
    "FA": "READ_CONTROL,DELETE,WRITE_DAC,WRITE_OWNER,SYNCHRONIZE,READ,WRITE,APPEND,READ_EXTENDED_ATTRIBUTES, \
WRITE_EXTENDED_ATTRIBUTES,EXECUTE,MEANINGLESS,READ_ATTRIBUTES,WRITE_ATTRIBUTES",
    "FR": "READ_CONTROL,READ,READ_ATTRIBUTES,READ_EXTENDED_ATTRIBUES,SYNCHRONIZE",
    "FW": "READ_CONTROL,WRITE,WRITE_ATTRIBUTES,WRITE_EXTENDED_ATTRIBUES,APPEND,SYNCHRONIZE",
    "FX": "READ_CONTROL,READ_ATTRIBUTES,EXECUTE,SYNCHRONIZE",
    "KA": "READ_CONTROL,DELETE,WRITE_DAC,WRITE_OWNER,QUERY,SET,CREATE_SUB_KEY,ENUM_SUB_KEYS,NOTIFY,CREATE_LINK",
    "KR": "READ_CONTROL,QUERY,ENUM_SUB_KEYS,NOTIFY",
    "KW": "READ_CONTROL,SET,CREATE_SUB_KEY",
    "KE": "READ_CONTROL,QUERY,ENUM_SUB_KEYS,NOTIFY"
}

TRUSTEES = {
    'AN': 'Anonymous',
    'AO': 'Account Operators',
    'AU': 'Authenticated Users',
    'BA': 'Administrators',
    'BG': 'Guests',
    'BO': 'Backup Operators',
    'BU': 'Users',
    'CA': 'Certificate Publishers',
    'CD': 'Certificate Services DCOM Access',
    'CG': 'Creator Group',
    'CO': 'Creator Owner',
    'DA': 'Domain Admins',
    'DC': 'Domain Computers',
    'DD': 'Domain Controllers',
    'DG': 'Domain Guests',
    'DU': 'Domain Users',
    'EA': 'Enterprise Admins',
    'ED': 'Enterprise Domain Controllers',
    'RO': 'Enterprise Read-Only Domain Controllers',
    'PA': 'Group Policy Admins',
    'IU': 'Interactive Users',
    'LA': 'Local Administrator',
    'LG': 'Local Guest',
    'LS': 'Local Service',
    'SY': 'Local System',
    'NU': 'Network',
    'LW': 'Low Integrity',
    'ME': 'Medium Integrity',
    'HI': 'High Integrity',
    'SI': 'System Integrity',
    'NO': 'Network Configuration Operators',
    'NS': 'Network Service',
    'PO': 'Printer Operators',
    'PS': 'Self',
    'PU': 'Power Users',
    'RS': 'RAS Servers',
    'RD': 'Remote Desktop Users',
    'RE': 'Replicator',
    'RC': 'Restricted Code',
    'RU': 'Pre-Win2k Compatibility Access',
    'SA': 'Schema Administrators',
    'SO': 'Server Operators',
    'SU': 'Service',
    'WD': 'Everyone',
    'WR': 'Write restricted Code',
}

ACCESS_MASK_HEX = dict([
    (0x10000000, 'GA'),
    (0x20000000, 'GX'),
    (0x40000000, 'GW'),
    (0x80000000, 'GR'),

    (0x00010000, 'SD'),
    (0x00020000, 'RC'),
    (0x00040000, 'WD'),
    (0x00080000, 'WO'),

    (0x00000001, 'CC'),
    (0x00000002, 'DC'),
    (0x00000004, 'LC'),
    (0x00000008, 'SW'),
    (0x00000010, 'RP'),
    (0x00000020, 'WP'),
    (0x00000040, 'DT'),
    (0x00000080, 'LO'),
    (0x00000100, 'CR'),

    (0x000f01ff, 'FA'),
    (0x00020089, 'FR'),
    (0x00020116, 'FW'),
    (0x000200a0, 'FX'),

    (0x000f003f, 'KA'),
    (0x00020019, 'KR'),
    (0x00020006, 'KW'),
    (0x00020019, 'KE')
])

ACCESS_MASK_HEX_REVERSE = dict([
    ('GA', 0x10000000),
    ('GX', 0x20000000),
    ('GW', 0x40000000),
    ('GR', 0x80000000),

    ('SD', 0x00010000),
    ('RC', 0x00020000),
    ('WD', 0x00040000),
    ('WO', 0x00080000),

    ('CC', 0x00000001),
    ('DC', 0x00000002),
    ('LC', 0x00000004),
    ('SW', 0x00000008),
    ('RP', 0x00000010),
    ('WP', 0x00000020),
    ('DT', 0x00000040),
    ('LO', 0x00000080),
    ('CR', 0x00000100),

    ('FA', 0x000f01ff),
    ('FR', 0x00020089),
    ('FW', 0x00020116),
    ('FX', 0x000200a0),

    ('KA', 0x000f003f),
    ('KR', 0x00020019),
    ('KW', 0x00020006),
    ('KE', 0x00020019)
])

PERM_TYPE_MAPPING = {
    'file':             dict(GENERIC_PERMISSIONS, **PERMISSIONS_FILE),
    'directory':        dict(GENERIC_PERMISSIONS, **PERMISSIONS_DIRECTORY),
    'file_map':         dict(GENERIC_PERMISSIONS, **PERMISSIONS_FILE_MAP),
    'registry':         dict(GENERIC_PERMISSIONS, **PERMISSIONS_REGISTRY),
    'service':          dict(GENERIC_PERMISSIONS, **PERMISSIONS_SERVICE),
    'service_control':  dict(GENERIC_PERMISSIONS, **PERMISSIONS_SERVICE_CONTROL),
    'process':          dict(GENERIC_PERMISSIONS, **PERMISSIONS_PROCESS),
    'thread':           dict(GENERIC_PERMISSIONS, **PERMISSIONS_THREAD),
    'window_station':   dict(GENERIC_PERMISSIONS, **PERMISSIONS_WINDOW_STATION),
    'desktop':          dict(GENERIC_PERMISSIONS, **PERMISSIONS_DESKTOP),
    'pipe':             dict(GENERIC_PERMISSIONS, **PERMISSIONS_PIPE),
    'token':            dict(GENERIC_PERMISSIONS, **PERMISSIONS_TOKEN),
}
