workflow_config = {
  "deduplicate_clip_to_footprint": False,
  "dir_input": "/data/viz_workflow/lakes/input/",
  "ext_input": ".gpkg",
  "dir_staged": "/data/viz_workflow/lakes/output/staged/",
  "dir_geotiff": "/data/viz_workflow/lakes/output/geotiff/",
  "dir_web_tiles": "/data/viz_workflow/lakes/output/web_tiles/",
  "filename_staging_summary": "/data/viz_workflow/lakes/output/staging_summary.csv",
  "filename_rasterization_events": "/data/viz_workflow/lakes/output/raster_events.csv",
  "filename_rasters_summary": "/data/viz_workflow/lakes/output/raster_summary.csv",
  "simplify_tolerance": 0.001,
  "tms_id": "WGS1984Quad",
  "z_range": [
    0,
    12
  ],
  "geometricError": 57,
  "z_coord": 0,
  "statistics": [
    {
      "name": "change_rate",
      "weight_by": "area",
      "property": "ChangeRateNet_myr-1",
      "aggregation_method": "min",
      "resampling_method": "mode",
      "val_range": [
        -2,
        2
      ],
      "palette": ["#ff0000", # red
                  "#FF8C00", # DarkOrange
                  "#FFA07A", # LightSalmon
                  "#FFFF00", # yellow
                  "#66CDAA", # MediumAquaMarine
                  "#AFEEEE", # PaleTurquoise,
                  "#0000ff"], # blue
      "nodata_val": 0,
      "nodata_color": "#ffffff00" # fully transparent white
    },
  ],
  # "deduplicate_at": ["raster"],
  "deduplicate_at": None,
  # "deduplicate_keep_rules": [["Perimeter_meter","larger"]], # [property, operator], using property with all positive values
  # "deduplicate_method": "neighbor",
  "deduplicate_method": None
  #"deduplicate_overlap_tolerance": 0.1,
  # "deduplicate_overlap_both": False,
  #"deduplicate_centroid_tolerance": None
}
