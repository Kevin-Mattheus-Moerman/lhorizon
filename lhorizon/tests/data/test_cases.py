from pathlib import Path

CYDONIA_PALM_SPRINGS_1959_TOPO = {
    "init_kwargs": {
        "target": {"lon": -9.46, "lat": 40.75, "elevation": 0, "body": 499},
        "origin": {"lon": -243.46, "lat": 33.8, "elevation": 0, "body": 399},
        "epochs": {
            "start": "1959-01-01T00:00:00",
            "stop": "1959-01-02T01:00:00",
            "step": "5m",
        },
    },
    "request_url": "https://ssd.jpl.nasa.gov/horizons_batch.cgi?batch=1"
    "&TABLE_TYPE=OBSERVER&QUANTITIES=%27A%27&COMMAND=%22g%3A"
    "-9.46%2C40.75%2C0%40499%22&SOLAR_ELONG=%220%2C180%22"
    "&LHA_CUTOFF=0&CSV_FORMAT=YES&CAL_FORMAT=BOTH&ANG_FORMAT"
    "=DEG&APPARENT=AIRLESS&REF_SYSTEM=J2000&EXTRA_PREC=NO"
    "&CENTER=coord%40399&COORD_TYPE=GEODETIC&SITE_COORD=%27"
    "-243.460000%2C33.800000%2C0.000000%27&START_TIME=%221959"
    "-01-01T00%3A00%3A00%22&STOP_TIME=%221959-01-02T01%3A00"
    "%3A00%22&STEP_SIZE=%225m%22&SKIP_DAYLT=NO",
    "data_path": str(Path(Path(__file__).parent, "CYDONIA_PALM_SPRINGS_1959_TOPO")),
    "table_columns": ('time', 'ra_ast', 'dec_ast', 'ra_app', 'dec_app', 'ra_app_icrf',
       'dec_app_icrf', 'az', 'alt', 'dist', 'sub_lon', 'sub_lat', 'ang_diam',
       't_o_m', 'npa'),
    'ra_ast_12_15': (44.99446, 44.99503, 44.99561)

}

MEUDON_MOON_NOW = {
    "init_kwargs": {
        "target": 301,
        "origin": "5@399",
    },
    "request_url": "https://ssd.jpl.nasa.gov/horizons_batch.cgi?batch=1"
    "&TABLE_TYPE=OBSERVER&QUANTITIES=%27A%27&COMMAND=%22301"
    "%22&SOLAR_ELONG=%220%2C180%22&LHA_CUTOFF=0&CSV_FORMAT"
    "=YES&CAL_FORMAT=BOTH&ANG_FORMAT=DEG&APPARENT=AIRLESS"
    "&REF_SYSTEM=J2000&EXTRA_PREC=NO&CENTER=%275%40399%27"
    "&TLIST=",
}

SUN_PHOBOS_1999 = {
    "init_kwargs": {
        "target": "Phobos",
        "origin": "@sun",
        "epochs": "1991-01-01",
    },
    "request_url": "https://ssd.jpl.nasa.gov/horizons_batch.cgi?batch=1"
    "&TABLE_TYPE=OBSERVER&QUANTITIES=%27A%27&COMMAND"
    "=%22Phobos%22&SOLAR_ELONG=%220%2C180%22&LHA_CUTOFF=0"
    "&CSV_FORMAT=YES&CAL_FORMAT=BOTH&ANG_FORMAT=DEG"
    "&APPARENT=AIRLESS&REF_SYSTEM=J2000&EXTRA_PREC=NO"
    "&CENTER=%27%40sun%27&TLIST=2448257.5&SKIP_DAYLT=NO",
    "df_columns": 'Date__(UT)__HR:MN:SC.fff,Date_________JDUT,R.A._(ICRF),'
                  'DEC_(ICRF),R.A._(a-app),DEC_(a-app),dRA*cosD,d(DEC)/dt,'
                  'Azi_(a-app),Elev_(a-app),dAZ*cosE,d(ELV)/dt,X_(sat-prim),'
                  'Y_(sat-prim),SatPANG,L_Ap_Sid_Time,a-mass,mag_ex,APmag,'
                  'S-brt,Illu%,Def_illu,ang-sep,vis.,Ang-diam,ObsSub-LON,'
                  'ObsSub-LAT,SunSub-LON,SunSub-LAT,SN.ang,SN.dist,NP.ang,'
                  'NP.dist,hEcl-Lon,hEcl-Lat,r,rdot,delta,deldot,'
                  '1-way_down_LT,VmagSn,VmagOb,S-O-T,/r,S-T-O,T-O-I,'
                  'IB_Illu%,O-P-T,PsAng,PsAMV,PlAng,Cnst,TDB-UT,ObsEcLon,'
                  'ObsEcLat,N.Pole-RA,N.Pole-DC,GlxLon,GlxLat,L_Ap_SOL_Time,'
                  '399_ins_LT,RA_3sigma,DEC_3sigma,SMAA_3sig,SMIA_3sig,'
                  'Theta,Area_3sig,POS_3sigma,RNG_3sigma,RNGRT_3sig,'
                  'DOP_S_3sig,DOP_X_3sig,RT_delay_3sig,Tru_Anom,'
                  'L_Ap_Hour_Ang,phi,PAB-LON,PAB-LAT,App_Lon_Sun,'
                  'RA_(ICRF-a-app),DEC_(ICRF-a-app),I_dRA*cosD,I_d(DEC)/dt',
    'App_Lon_Sun': 355.473752,
    'dist': 232353317922.06027,
    "data_path": str(Path(Path(__file__).parent, "SUN_PHOBOS_1999")),
}
