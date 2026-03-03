#!/bin/bash

# Hash that translates the names from source to target
declare -A files
files[oC_cloud_2_128]="OpenCloud_cloud"
files[oC_darkgreen_2_128]="OpenCloud_ok"
files[oC_error_2_128]="OpenCloud_error"
files[oC_lightgreen_2_128]="OpenCloud_lightok"
files[oC_share_2_128]="OpenCloud_share"
files[oC_sync_2_128]="OpenCloud_sync"
files[oC_warn_2_128]="OpenCloud_warn"

# Export dir
exp="exports"

for i in 16 32 48 64 72 128 256 512 1024 ; do
    dir="$exp/$i"x"$i"
    mkdir -p "$dir"

    for f in "${!files[@]}"; do
        src=$f
        target="${files[$f]}"

        inkscape -w $i -h $i --export-type=png --export-filename="$dir/$target" "$src.svg"
    done
done
