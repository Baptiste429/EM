import xarray as xr
print("Transformation des donées..")
file_path = "./euromillions-gamedata-FR-2025"
DS = xr.open_dataset(file_path + ".nc")
DS.to_dataframe().to_csv( file_path + ".csv")
print("donnée transformée")
