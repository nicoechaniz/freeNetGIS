# -*- coding: utf-8 -*-

PROTOCOL_CHANNELS = (
    ('802.11b (1-11Mbps - 2.4Ghz)', (
            ('0', 'Auto 2.4GHz'),
            ('1', '1 - 2412 MHz'),
            ('2', '2 - 2417 MHz'),
            ('3', '3 - 2422 MHz'),                        
            ('4', '4 - 2427 MHz'),
            ('5', '5 - 2432 MHz'),
            ('6', '6 - 2437 MHz'),
            ('7', '7 - 2442 MHz'),
            ('8', '8 - 2447 MHz'),                        
            ('9', '9 - 2452 MHz'),
            ('10', '10 - 2457 MHz'),        
            ('11', '11 - 2462 MHz'),
            ('12', '12 - 2467 MHz'),
            ('13', '13 - 2472 MHz'),                        
            ('14', '14 - 2477 MHz'),
        )
    ),
    ('802.11g (2-54Mbps - 2.4Ghz)', (
            ('0', 'Auto 2.4GHz'),
            ('1', '1 - 2412 MHz'),
            ('2', '2 - 2417 MHz'),
            ('3', '3 - 2422 MHz'),                        
            ('4', '4 - 2427 MHz'),
            ('5', '5 - 2432 MHz'),
            ('6', '6 - 2437 MHz'),
            ('7', '7 - 2442 MHz'),
            ('8', '8 - 2447 MHz'),                        
            ('9', '9 - 2452 MHz'),
            ('10', '10 - 2457 MHz'),        
            ('11', '11 - 2462 MHz'),
            ('12', '12 - 2467 MHz'),
            ('13', '13 - 2472 MHz'),                        
            ('14', '14 - 2477 MHz'),
        )
    ),
)

RADIO_MODE = (
    ('AP', 'AP or AP with WDS'),
    ('WC', 'Wireless Client'),
    ('WB', 'Wireless Bridge'),
    ('RC', 'Routed Client'),
)

ANTENNA_TYPE = (
    ('OR', 'Original / Integrated'),
    ('OM', 'Omnidirectional'),
    ('DI', 'Directional / Yagi'),
    ('SE', 'Sectorial / Patch'),
)

CONNECTOR_TYPE = (
    ('MA', 'Main / Right / Internal'),
    ('AU', 'Auxiliar / Left / External'),
)