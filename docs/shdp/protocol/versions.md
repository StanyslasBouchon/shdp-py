Module shdp.protocol.versions
=============================

Classes
-------

`Version(*args, **kwds)`
:   Protocol version enumeration.
    
    This enum represents the different versions of the protocol.
    The value of each version is automatically converted from 'VX' to integer X.
    
    Examples:
        >>> Version.V1.value
        1
        >>> Version.V1.name
        'V1'
        >>> str(Version.V1)
        'V1'

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `V1`
    :