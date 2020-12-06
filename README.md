## Converting ABF/DAT files to NWB

The script `x-to-nwb` allows to convert ABF/DAT files to NeurodataWithoutBorders v2 files.

For programmatic use the function `convert` is designed as public interface.

```python
from x_to_nwb import convert
help(convert)
```

### ABF specialities

As of 9/2018 PClamp/Clampex does not record all required amplifier settings.
For gathering these please see the `mcc_get_settings.py` script in the ipfx
repository which gathers all amplifier settings from all active amplifiers and
writes them to a file in JSON output.

In case you don't have a JSON settings file pass `--no-searchSettingsFile` to avoid warnings.

By default all AD and DA channels are outputted into the NWB file. You can
select to only export some AD channels with

```sh
x-to-nwb --includeChannel ABCD 2018_03_20_0000.abf
```

Or to discard some AD channels use

```sh
x-to-nwb --discardChannel ABCD 2018_03_20_0000.abf
```

#### Required input files

- ABF files acquired with Clampex/pCLAMP.
- If custom waveforms are used for the stimulus protocol, the source ATF files are required as well.

#### Examples

##### Convert a single file

```sh
x-to-nwb 2018_03_20_0000.abf
```

##### Convert a single file with overwrite and use a directory for finding custom waveforms

Some acquired data might use custom wave forms for defining the stimulus
protocols. These custom waveforms are stored in external files and don't reside
in the ABF files. We therefore allow the user to pass a directory where
these files should be searched. Currently only custom waveforms in ATF (Axon
Text format) are supported.

```sh
x-to-nwb --overwrite --protocolDir protocols 2018_03_20_0000.abf
```

##### Convert a folder with ABF files

The following command converts all ABF files which reside in `someFolder` to a single NWB file.

```sh
x-to-nwb --fileType ".abf" --overwrite someFolder
```

#### Disabling compression

The following command disables compression of the HDF5 datasets (intended for debugging purposes).

```sh
x-to-nwb --no-compression 2018_03_20_0000.abf
```

### DAT specialities

#### Required input files

DAT files acquired with Patchmaster version 2x90.

#### Examples

##### Convert a single file creating one NWB file per Group

```sh
x-to-nwb H18.28.015.11.12.dat
```

##### Convert a single file creating one NWB file with all Groups

```sh
x-to-nwb --multipleGroupsPerFile H18.28.015.11.12.dat
```

## Outputting DAT/ABF metadata files for debugging purposes

```sh
x-to-nwb --outputMetadata *.dat *.abf
```

## Running the regression tests

Currently only file level regressions tests exist which check that the
conversion from DAT/ABF to NWB results in the same NWB files compared to earlier
versions.

For running the tests do the following:

```sh
cd tests
py.test --collect-only .
py.test --numprocesses auto .
```

The separate collection step is necessary as that can not be parallelized, see also
https://github.com/pytest-dev/pytest-xdist/issues/18.
