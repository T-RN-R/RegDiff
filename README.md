# Registry Diff


This is an in progress registry differ that produces reports of interesting changes  to the Windows registry



See [This Example](SYSTEM_WIN11.md) for a sample report. Only the SYSTEM hive is currently supported in reports ( however any hive may be diffed and dumped to json).

Reports currently report on the following information:

- ControlSet001\\Control\\Services
- ControlSet001\\Control\\WMI\\AutoLogger

TODO:

    - Write a Firewall Rule parser
    - Add reporting for SOFTWARE , COMPONENTS and DRIVERS hives.
    - Add reporting support for the following SYSTEM keys:
        - ControlSet001\\Control\\Cryptography"
        - ControlSet001\\Control\\Class\\
        - ControlSet001\\Control\\CI\\"
        - ControlSet001\\Control\\Tpm
        - ControlSet001\\Control\\SafeBoot
        - ControlSet001\\Control\\Session Manager
        - ControlSet001\\Control\\WMI\\Security
        - ControlSet001\\Control\\FileSystem
        - ControlSet001\\Control\\FeatureManagement
