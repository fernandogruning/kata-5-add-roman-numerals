# Documento de Requerimientos
Python

## Requerimientos
*REQ-1*: El algoritmo realiza la operación de suma de la entrada de uno o más números romanos y tiene como salida el resultado de la suma como número normal.

## Criterios de Aceptación
*CRI-1-1*: El algoritmo debe aceptar como parámetro uno o más strings de números romanos válidos.
*CRI-1-2*: El algoritmo debe convertir dichos parámetros a sus representaciones numéricas.
*CRI-1-3*: El algoritmo debe retornar la suma de los parámetros dados.

## Escenarios de Pruebas
*SCE-1-1-1*: `addRomanNumerals(“”)` debe retornar `0`.
*SCE-1-1-2*: `addRomanNumerasl(“IV”)` debe retornar `4`.
*SCE-1-1-3*: `addRomanNumerals(“XIII”)` debe retornar `13`.
*SCE-1-2-1*: `convertRomanNumeral(“I”)` debe retornar `1`.
*SCE-1-2-2*: `convertRomanNumeral(“IX”)` debe retornar `4`.
*SCE-1-2-3*: `convertRomanNumeral(“XIV”)` debe retornar `9`.
*SCE-1-3-1*: `addRomanNumerals(“I”)` debe retornar `1`.
*SCE-1-3-2*: `addRomanNumerals(“I”, “III”)` debe retornar `4`.
*SCE-1-3-3*: `addRomanNumerals(“XIII”, “IX”, “XIV”)` debe retornar `36`.
