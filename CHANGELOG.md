# Changelog

## 0.1.0-alpha.21 (2025-03-14)

Full Changelog: [v0.1.0-alpha.20...v0.1.0-alpha.21](https://github.com/clear-street/studio-sdk-python/compare/v0.1.0-alpha.20...v0.1.0-alpha.21)

### Features

* **api:** add net pnl to pnl-sums ([#128](https://github.com/clear-street/studio-sdk-python/issues/128)) ([fe6d7a8](https://github.com/clear-street/studio-sdk-python/commit/fe6d7a87d10c770d4d29cd98f66524dbf284a2ee))


### Chores

* **docs:** update client docstring ([#124](https://github.com/clear-street/studio-sdk-python/issues/124)) ([3a6ead4](https://github.com/clear-street/studio-sdk-python/commit/3a6ead4321066ff89f100414d5a0fe915690f9eb))
* **internal:** remove extra empty newlines ([#129](https://github.com/clear-street/studio-sdk-python/issues/129)) ([65ae44d](https://github.com/clear-street/studio-sdk-python/commit/65ae44d2b97b84efefed20933d4c64b978c12ebd))
* **internal:** remove unused http client options forwarding ([#126](https://github.com/clear-street/studio-sdk-python/issues/126)) ([f846263](https://github.com/clear-street/studio-sdk-python/commit/f8462631f122309e75838e93f39d7db0271de5ce))


### Documentation

* update URLs from stainlessapi.com to stainless.com ([#123](https://github.com/clear-street/studio-sdk-python/issues/123)) ([6298367](https://github.com/clear-street/studio-sdk-python/commit/62983675f0719e3cf4892d4baaf88df3f9671459))

## 0.1.0-alpha.20 (2025-02-26)

Full Changelog: [v0.1.0-alpha.19...v0.1.0-alpha.20](https://github.com/clear-street/studio-sdk-python/compare/v0.1.0-alpha.19...v0.1.0-alpha.20)

### Features

* **api:** fix tests ([#117](https://github.com/clear-street/studio-sdk-python/issues/117)) ([722d6f5](https://github.com/clear-street/studio-sdk-python/commit/722d6f54a5ee9c6683c52660a55ce907084cc436))
* **api:** manual updates ([#114](https://github.com/clear-street/studio-sdk-python/issues/114)) ([666eef4](https://github.com/clear-street/studio-sdk-python/commit/666eef45717ccab2e25aec47e4d15ef8ce3ccac2))
* **api:** manual updates ([#116](https://github.com/clear-street/studio-sdk-python/issues/116)) ([40e369e](https://github.com/clear-street/studio-sdk-python/commit/40e369e2d70ac9c59c74db1f5f17ec6c247bd739))
* **api:** manual updates ([#121](https://github.com/clear-street/studio-sdk-python/issues/121)) ([2089f2b](https://github.com/clear-street/studio-sdk-python/commit/2089f2b59a96a8a29b1b83b866eb963aebd70f53))
* **client:** allow passing `NotGiven` for body ([#118](https://github.com/clear-street/studio-sdk-python/issues/118)) ([6682a49](https://github.com/clear-street/studio-sdk-python/commit/6682a492f6137a31f5cd57e9e1c2ec94539ec325))


### Bug Fixes

* **client:** mark some request bodies as optional ([6682a49](https://github.com/clear-street/studio-sdk-python/commit/6682a492f6137a31f5cd57e9e1c2ec94539ec325))


### Chores

* **internal:** fix devcontainers setup ([#119](https://github.com/clear-street/studio-sdk-python/issues/119)) ([6e43e2a](https://github.com/clear-street/studio-sdk-python/commit/6e43e2af7bb5a031146b7c50bf8849a4c87c18fa))
* **internal:** properly set __pydantic_private__ ([#120](https://github.com/clear-street/studio-sdk-python/issues/120)) ([df9ac8c](https://github.com/clear-street/studio-sdk-python/commit/df9ac8c737f8a240b62fe10fdbc5e49df102780a))

## 0.1.0-alpha.19 (2025-02-19)

Full Changelog: [v0.1.0-alpha.18...v0.1.0-alpha.19](https://github.com/clear-street/studio-sdk-python/compare/v0.1.0-alpha.18...v0.1.0-alpha.19)

### Features

* **api:** remove symbol filtering from pnl-sums ([#111](https://github.com/clear-street/studio-sdk-python/issues/111)) ([ed079d9](https://github.com/clear-street/studio-sdk-python/commit/ed079d91b4521e97ffd28184a31cb7da73af67a2))

## 0.1.0-alpha.18 (2025-02-14)

Full Changelog: [v0.1.0-alpha.17...v0.1.0-alpha.18](https://github.com/clear-street/studio-sdk-python/compare/v0.1.0-alpha.17...v0.1.0-alpha.18)

### Features

* **client:** send `X-Stainless-Read-Timeout` header ([#106](https://github.com/clear-street/studio-sdk-python/issues/106)) ([8357a68](https://github.com/clear-street/studio-sdk-python/commit/8357a685952e2f52457ee7c518bf7214191cb7b6))


### Bug Fixes

* **api:** better support union schemas with common properties ([#95](https://github.com/clear-street/studio-sdk-python/issues/95)) ([7ea9b5e](https://github.com/clear-street/studio-sdk-python/commit/7ea9b5ed2d55c42e6bda4ac896ef73d665cbba53))
* asyncify on non-asyncio runtimes ([#109](https://github.com/clear-street/studio-sdk-python/issues/109)) ([37e16e8](https://github.com/clear-street/studio-sdk-python/commit/37e16e870b782fc246b8ce8d52d5819cd53614b4))
* **client:** only call .close() when needed ([#92](https://github.com/clear-street/studio-sdk-python/issues/92)) ([090806b](https://github.com/clear-street/studio-sdk-python/commit/090806b20ea46fac9dd170feb98fe95ad26ebd8b))
* correctly handle deserialising `cls` fields ([#96](https://github.com/clear-street/studio-sdk-python/issues/96)) ([13bed11](https://github.com/clear-street/studio-sdk-python/commit/13bed116c380e0e3215f61258e5b70dce5d45b4c))
* deduplicate unknown entries in union ([#103](https://github.com/clear-street/studio-sdk-python/issues/103)) ([25b27e4](https://github.com/clear-street/studio-sdk-python/commit/25b27e43024e634be0a72828cfbe3299e04757b3))
* **tests:** make test_get_platform less flaky ([#99](https://github.com/clear-street/studio-sdk-python/issues/99)) ([050518d](https://github.com/clear-street/studio-sdk-python/commit/050518d93ff9630513144f97b14b584e1ee7b3cf))


### Chores

* **internal:** avoid pytest-asyncio deprecation warning ([#100](https://github.com/clear-street/studio-sdk-python/issues/100)) ([a66fba3](https://github.com/clear-street/studio-sdk-python/commit/a66fba3c87fa8d9aedcd09b1b02760c95ab19b14))
* **internal:** bummp ruff dependency ([#105](https://github.com/clear-street/studio-sdk-python/issues/105)) ([dbc4dbe](https://github.com/clear-street/studio-sdk-python/commit/dbc4dbe30fdb70b118e9542206f4eb27a618b76d))
* **internal:** bump httpx dependency ([#91](https://github.com/clear-street/studio-sdk-python/issues/91)) ([a836521](https://github.com/clear-street/studio-sdk-python/commit/a836521e7456b1b88bfcc88939a859219810c7e2))
* **internal:** change default timeout to an int ([#104](https://github.com/clear-street/studio-sdk-python/issues/104)) ([ca6afef](https://github.com/clear-street/studio-sdk-python/commit/ca6afef849107703318baccefbe95b2ce24d0154))
* **internal:** codegen related update ([#101](https://github.com/clear-street/studio-sdk-python/issues/101)) ([3b949f4](https://github.com/clear-street/studio-sdk-python/commit/3b949f4a066d84e59e09133174bde5663b1f27c6))
* **internal:** codegen related update ([#88](https://github.com/clear-street/studio-sdk-python/issues/88)) ([dc24ced](https://github.com/clear-street/studio-sdk-python/commit/dc24ced22ec76d09b3ae9aa33abc91e432733572))
* **internal:** codegen related update ([#90](https://github.com/clear-street/studio-sdk-python/issues/90)) ([28907db](https://github.com/clear-street/studio-sdk-python/commit/28907db57dd0a72601d01676fef5316620b12144))
* **internal:** codegen related update ([#94](https://github.com/clear-street/studio-sdk-python/issues/94)) ([f5d8750](https://github.com/clear-street/studio-sdk-python/commit/f5d87505d08ffdacb49f6c71984c9c3a9b4e4585))
* **internal:** codegen related update ([#97](https://github.com/clear-street/studio-sdk-python/issues/97)) ([4144402](https://github.com/clear-street/studio-sdk-python/commit/4144402d212358d70747707a04e21510569b104c))
* **internal:** fix type traversing dictionary params ([#107](https://github.com/clear-street/studio-sdk-python/issues/107)) ([fd4d52f](https://github.com/clear-street/studio-sdk-python/commit/fd4d52f99e68933e8e5614acdbf654dfd86e3fbd))
* **internal:** minor formatting changes ([#102](https://github.com/clear-street/studio-sdk-python/issues/102)) ([fab8f46](https://github.com/clear-street/studio-sdk-python/commit/fab8f46801884580af849f15d0429ff2a95fc17d))
* **internal:** minor type handling changes ([#108](https://github.com/clear-street/studio-sdk-python/issues/108)) ([9f77dd3](https://github.com/clear-street/studio-sdk-python/commit/9f77dd37a1f892a83103cef46f8fb2d1e0de7450))


### Documentation

* fix typos ([#93](https://github.com/clear-street/studio-sdk-python/issues/93)) ([f142e41](https://github.com/clear-street/studio-sdk-python/commit/f142e41861709d140f3cfccf1be2e459f27ba291))
* **raw responses:** fix duplicate `the` ([#98](https://github.com/clear-street/studio-sdk-python/issues/98)) ([d6f1bdd](https://github.com/clear-street/studio-sdk-python/commit/d6f1bddd4c1b59386f6883c786f5771f63dd314d))

## 0.1.0-alpha.17 (2024-12-19)

Full Changelog: [v0.1.0-alpha.16...v0.1.0-alpha.17](https://github.com/clear-street/studio-sdk-python/compare/v0.1.0-alpha.16...v0.1.0-alpha.17)

### Features

* **api:** add average cost to positions ([#85](https://github.com/clear-street/studio-sdk-python/issues/85)) ([c27bd79](https://github.com/clear-street/studio-sdk-python/commit/c27bd798d73b28ec32f6dc4b207dd7379a20a24b))

## 0.1.0-alpha.16 (2024-12-18)

Full Changelog: [v0.1.0-alpha.15...v0.1.0-alpha.16](https://github.com/clear-street/studio-sdk-python/compare/v0.1.0-alpha.15...v0.1.0-alpha.16)

### Chores

* **internal:** add support for TypeAliasType ([#80](https://github.com/clear-street/studio-sdk-python/issues/80)) ([174dfac](https://github.com/clear-street/studio-sdk-python/commit/174dfac4c311728e5e80dd60828671248078a8d8))
* **internal:** bump pydantic dependency ([#76](https://github.com/clear-street/studio-sdk-python/issues/76)) ([9f6bfa1](https://github.com/clear-street/studio-sdk-python/commit/9f6bfa14408def30dcc33d4953faf017111b75a8))
* **internal:** bump pyright ([#79](https://github.com/clear-street/studio-sdk-python/issues/79)) ([78f1099](https://github.com/clear-street/studio-sdk-python/commit/78f10998fab7d9789b01e8c68e9c376cef802189))
* **internal:** codegen related update ([#81](https://github.com/clear-street/studio-sdk-python/issues/81)) ([5ebf768](https://github.com/clear-street/studio-sdk-python/commit/5ebf7684b4a459b3c070df3758bab4ce4ae4fac7))
* **internal:** fix some typos ([#83](https://github.com/clear-street/studio-sdk-python/issues/83)) ([2f9c6fa](https://github.com/clear-street/studio-sdk-python/commit/2f9c6faa24900512a7b40c25256fe8dee0d5003b))


### Documentation

* **readme:** example snippet for client context manager ([#82](https://github.com/clear-street/studio-sdk-python/issues/82)) ([6d2b4a7](https://github.com/clear-street/studio-sdk-python/commit/6d2b4a7060ca8d6652ea559760657c58e7be0618))
* **readme:** fix http client proxies example ([#78](https://github.com/clear-street/studio-sdk-python/issues/78)) ([d3e3918](https://github.com/clear-street/studio-sdk-python/commit/d3e3918a7e9e29776a017fc06ee2ed6c762eaec2))

## 0.1.0-alpha.15 (2024-12-09)

Full Changelog: [v0.1.0-alpha.14...v0.1.0-alpha.15](https://github.com/clear-street/studio-sdk-python/compare/v0.1.0-alpha.14...v0.1.0-alpha.15)

### Features

* **api:** account number support ([#74](https://github.com/clear-street/studio-sdk-python/issues/74)) ([c91236d](https://github.com/clear-street/studio-sdk-python/commit/c91236de909214b523701b83e10eb3366a7ec426))


### Chores

* **internal:** bump pyright ([#71](https://github.com/clear-street/studio-sdk-python/issues/71)) ([75e4f25](https://github.com/clear-street/studio-sdk-python/commit/75e4f25fcca33bae792841c978ea66c29b8db61a))

## 0.1.0-alpha.14 (2024-11-29)

Full Changelog: [v0.1.0-alpha.13...v0.1.0-alpha.14](https://github.com/clear-street/studio-sdk-python/compare/v0.1.0-alpha.13...v0.1.0-alpha.14)

### Features

* **api:** add modify orders endpoint ([#68](https://github.com/clear-street/studio-sdk-python/issues/68)) ([f02195a](https://github.com/clear-street/studio-sdk-python/commit/f02195a6256c88d28b4cd967d3a5b411ac86654a))

## 0.1.0-alpha.13 (2024-11-28)

Full Changelog: [v0.1.0-alpha.12...v0.1.0-alpha.13](https://github.com/clear-street/studio-sdk-python/compare/v0.1.0-alpha.12...v0.1.0-alpha.13)

### Bug Fixes

* **client:** compat with new httpx 0.28.0 release ([#66](https://github.com/clear-street/studio-sdk-python/issues/66)) ([0586398](https://github.com/clear-street/studio-sdk-python/commit/0586398d10ecc772be8d75283162bb22fea4a073))


### Chores

* **internal:** codegen related update ([#64](https://github.com/clear-street/studio-sdk-python/issues/64)) ([02d56d8](https://github.com/clear-street/studio-sdk-python/commit/02d56d8e51138b0233039763ef0a48980dbb17c3))
* **internal:** codegen related update ([#65](https://github.com/clear-street/studio-sdk-python/issues/65)) ([f23970d](https://github.com/clear-street/studio-sdk-python/commit/f23970d3be640a2f75909c5709c8048617e874e9))
* **internal:** fix compat model_dump method when warnings are passed ([#63](https://github.com/clear-street/studio-sdk-python/issues/63)) ([e5874f8](https://github.com/clear-street/studio-sdk-python/commit/e5874f89c9b06e01288f03c35421c751dee5ec0f))
* **internal:** version bump ([#56](https://github.com/clear-street/studio-sdk-python/issues/56)) ([87913d2](https://github.com/clear-street/studio-sdk-python/commit/87913d2c81c926ab7e9e051b0a26c9e91cf32932))
* rebuild project due to codegen change ([#58](https://github.com/clear-street/studio-sdk-python/issues/58)) ([0dcf41f](https://github.com/clear-street/studio-sdk-python/commit/0dcf41f9015287afd18a8718c83403573a685201))
* rebuild project due to codegen change ([#59](https://github.com/clear-street/studio-sdk-python/issues/59)) ([569c4cd](https://github.com/clear-street/studio-sdk-python/commit/569c4cd8025b04e6dad8fbfacdca7bb71bbaf4d3))
* rebuild project due to codegen change ([#60](https://github.com/clear-street/studio-sdk-python/issues/60)) ([904d865](https://github.com/clear-street/studio-sdk-python/commit/904d8650ff6aa09e031901901d91f546469a8bc6))
* rebuild project due to codegen change ([#61](https://github.com/clear-street/studio-sdk-python/issues/61)) ([e4fa147](https://github.com/clear-street/studio-sdk-python/commit/e4fa14758305145cdb11ae802d486e54cfa574c5))
* rebuild project due to codegen change ([#62](https://github.com/clear-street/studio-sdk-python/issues/62)) ([de76347](https://github.com/clear-street/studio-sdk-python/commit/de76347c8e121c6c6df789287663e2c43661332e))

## 0.1.0-alpha.12 (2024-10-25)

Full Changelog: [v0.1.0-alpha.11...v0.1.0-alpha.12](https://github.com/clear-street/studio-sdk-python/compare/v0.1.0-alpha.11...v0.1.0-alpha.12)

### Features

* **api:** enable inventories endpoint ([#54](https://github.com/clear-street/studio-sdk-python/issues/54)) ([8fc74d6](https://github.com/clear-street/studio-sdk-python/commit/8fc74d66d9b93ab77093788b9f29c56fcfff1478))

## 0.1.0-alpha.11 (2024-10-11)

Full Changelog: [v0.1.0-alpha.10...v0.1.0-alpha.11](https://github.com/clear-street/studio-sdk-python/compare/v0.1.0-alpha.10...v0.1.0-alpha.11)

### Features

* **api:** api update ([#51](https://github.com/clear-street/studio-sdk-python/issues/51)) ([c594d64](https://github.com/clear-street/studio-sdk-python/commit/c594d64497b66ccbb6c4c6b10d8289094c2f12f0))

## 0.1.0-alpha.10 (2024-10-04)

Full Changelog: [v0.1.0-alpha.9...v0.1.0-alpha.10](https://github.com/clear-street/studio-sdk-python/compare/v0.1.0-alpha.9...v0.1.0-alpha.10)

### Features

* **api:** Add DMA and Stop Limit order support ([#45](https://github.com/clear-street/studio-sdk-python/issues/45)) ([1d8b0f5](https://github.com/clear-street/studio-sdk-python/commit/1d8b0f543dab7d35d6908583edbfb026e51d34ea))


### Chores

* add docstrings to raw response properties ([#42](https://github.com/clear-street/studio-sdk-python/issues/42)) ([f3c5945](https://github.com/clear-street/studio-sdk-python/commit/f3c594585a75c230018666923cab99c6570ad76d))
* **internal:** add support for parsing bool response content ([#49](https://github.com/clear-street/studio-sdk-python/issues/49)) ([fd1db20](https://github.com/clear-street/studio-sdk-python/commit/fd1db2031cdec661134ec10b0094c93e9489ede9))
* **internal:** codegen related update ([#46](https://github.com/clear-street/studio-sdk-python/issues/46)) ([094f3bf](https://github.com/clear-street/studio-sdk-python/commit/094f3bf0f68e2ac0143cc677222da2f289eecd33))
* **internal:** codegen related update ([#47](https://github.com/clear-street/studio-sdk-python/issues/47)) ([e01fdcf](https://github.com/clear-street/studio-sdk-python/commit/e01fdcfa63265e92171fc1502f5c298e8d2b07ac))
* **internal:** codegen related update ([#48](https://github.com/clear-street/studio-sdk-python/issues/48)) ([025b0ba](https://github.com/clear-street/studio-sdk-python/commit/025b0bace9e15f2faea93f960408a202ca500861))


### Documentation

* **readme:** add section on determining installed version ([#44](https://github.com/clear-street/studio-sdk-python/issues/44)) ([cb5137b](https://github.com/clear-street/studio-sdk-python/commit/cb5137bb1c742b9a5143d5e094328e114807d967))

## 0.1.0-alpha.9 (2024-09-05)

Full Changelog: [v0.1.0-alpha.8...v0.1.0-alpha.9](https://github.com/clear-street/studio-sdk-python/compare/v0.1.0-alpha.8...v0.1.0-alpha.9)

### Features

* **api:** add sandbox url ([#36](https://github.com/clear-street/studio-sdk-python/issues/36)) ([8a98682](https://github.com/clear-street/studio-sdk-python/commit/8a98682938297f756a7560f3fa76daf083b4cbe8))


### Chores

* pyproject.toml formatting changes ([#37](https://github.com/clear-street/studio-sdk-python/issues/37)) ([927355c](https://github.com/clear-street/studio-sdk-python/commit/927355cf8e5dc6f62a515e1a91b1cf5604d17002))

## 0.1.0-alpha.8 (2024-08-30)

Full Changelog: [v0.1.0-alpha.7...v0.1.0-alpha.8](https://github.com/clear-street/studio-sdk-python/compare/v0.1.0-alpha.7...v0.1.0-alpha.8)

### Features

* **api:** update via SDK Studio ([#32](https://github.com/clear-street/studio-sdk-python/issues/32)) ([5260d3e](https://github.com/clear-street/studio-sdk-python/commit/5260d3e7fe0eb4b9ff729024642bb610a1b3de0f))

## 0.1.0-alpha.7 (2024-08-30)

Full Changelog: [v0.1.0-alpha.6...v0.1.0-alpha.7](https://github.com/clear-street/studio-sdk-python/compare/v0.1.0-alpha.6...v0.1.0-alpha.7)

### Features

* **api:** update via SDK Studio ([#29](https://github.com/clear-street/studio-sdk-python/issues/29)) ([17f2890](https://github.com/clear-street/studio-sdk-python/commit/17f28905246026b609f4be5c9832841806b5b98e))

## 0.1.0-alpha.6 (2024-08-27)

Full Changelog: [v0.1.0-alpha.5...v0.1.0-alpha.6](https://github.com/clear-street/studio-sdk-python/compare/v0.1.0-alpha.5...v0.1.0-alpha.6)

### Features

* **api:** update via SDK Studio ([#24](https://github.com/clear-street/studio-sdk-python/issues/24)) ([8fa6704](https://github.com/clear-street/studio-sdk-python/commit/8fa670458778503f137ef47a7671f39458a1e703))
* **api:** update via SDK Studio ([#26](https://github.com/clear-street/studio-sdk-python/issues/26)) ([d8f0eaf](https://github.com/clear-street/studio-sdk-python/commit/d8f0eaf1f17bb917def83aa977f849a7778157c7))


### Chores

* **internal:** codegen related update ([#27](https://github.com/clear-street/studio-sdk-python/issues/27)) ([4f61919](https://github.com/clear-street/studio-sdk-python/commit/4f61919c5a8fa360628dfd5d0b69e803ba18968d))

## 0.1.0-alpha.5 (2024-07-10)

Full Changelog: [v0.1.0-alpha.4...v0.1.0-alpha.5](https://github.com/clear-street/studio-sdk-python/compare/v0.1.0-alpha.4...v0.1.0-alpha.5)

### Features

* **api:** update via SDK Studio ([#21](https://github.com/clear-street/studio-sdk-python/issues/21)) ([52b6025](https://github.com/clear-street/studio-sdk-python/commit/52b6025ccbfbbace2963449d55ab5ef7c20c50c0))

## 0.1.0-alpha.4 (2024-07-10)

Full Changelog: [v0.1.0-alpha.3...v0.1.0-alpha.4](https://github.com/clear-street/studio-sdk-python/compare/v0.1.0-alpha.3...v0.1.0-alpha.4)

### Features

* **api:** update via SDK Studio ([#18](https://github.com/clear-street/studio-sdk-python/issues/18)) ([80d77f9](https://github.com/clear-street/studio-sdk-python/commit/80d77f9fec5e0409f1896ac9c7db9969932a87b6))

## 0.1.0-alpha.3 (2024-07-10)

Full Changelog: [v0.1.0-alpha.2...v0.1.0-alpha.3](https://github.com/clear-street/studio-sdk-python/compare/v0.1.0-alpha.2...v0.1.0-alpha.3)

### Features

* **api:** update via SDK Studio ([#10](https://github.com/clear-street/studio-sdk-python/issues/10)) ([284ea5b](https://github.com/clear-street/studio-sdk-python/commit/284ea5b1cae0af30bcd78cdc0048d3ec655312f7))
* **api:** update via SDK Studio ([#11](https://github.com/clear-street/studio-sdk-python/issues/11)) ([796f671](https://github.com/clear-street/studio-sdk-python/commit/796f671499be4027923046db555c1119a4fa1b30))
* **api:** update via SDK Studio ([#12](https://github.com/clear-street/studio-sdk-python/issues/12)) ([4f42bdc](https://github.com/clear-street/studio-sdk-python/commit/4f42bdc10992f6158c865781a0bdc70ae79b58e4))
* **api:** update via SDK Studio ([#13](https://github.com/clear-street/studio-sdk-python/issues/13)) ([6a92603](https://github.com/clear-street/studio-sdk-python/commit/6a926036a955e0d5ce12a3b1ee7a01ca88698a20))
* **api:** update via SDK Studio ([#14](https://github.com/clear-street/studio-sdk-python/issues/14)) ([181db49](https://github.com/clear-street/studio-sdk-python/commit/181db499eb8ba91afbf899bd2900d9893c4a941e))
* **api:** update via SDK Studio ([#15](https://github.com/clear-street/studio-sdk-python/issues/15)) ([db742cc](https://github.com/clear-street/studio-sdk-python/commit/db742cc51159f5c9838c4695c84ed38d8f9df665))
* **api:** update via SDK Studio ([#16](https://github.com/clear-street/studio-sdk-python/issues/16)) ([ca129f2](https://github.com/clear-street/studio-sdk-python/commit/ca129f2406b8e307a0f9c866d3433f901252bdfd))
* **api:** update via SDK Studio ([#7](https://github.com/clear-street/studio-sdk-python/issues/7)) ([540756e](https://github.com/clear-street/studio-sdk-python/commit/540756eb7ce95eb3404ae9873ccfc310b1f52cac))
* **api:** update via SDK Studio ([#9](https://github.com/clear-street/studio-sdk-python/issues/9)) ([5f6f844](https://github.com/clear-street/studio-sdk-python/commit/5f6f844097eeb52a6dad6a8e22676a4f84848c02))

## 0.1.0-alpha.2 (2024-07-09)

Full Changelog: [v0.1.0-alpha.1...v0.1.0-alpha.2](https://github.com/clear-street/studio-sdk-python/compare/v0.1.0-alpha.1...v0.1.0-alpha.2)

### Features

* **api:** update via SDK Studio ([#4](https://github.com/clear-street/studio-sdk-python/issues/4)) ([79921e2](https://github.com/clear-street/studio-sdk-python/commit/79921e2868a8931446c4f65f1abc994467105f17))

## 0.1.0-alpha.1 (2024-07-09)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/clear-street/studio-sdk-python/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* **api:** update via SDK Studio ([#3](https://github.com/clear-street/studio-sdk-python/issues/3)) ([e1c1399](https://github.com/clear-street/studio-sdk-python/commit/e1c139959000be1f7d171e08b8e3b024f61f64f9))


### Chores

* configure new SDK language ([7d853cb](https://github.com/clear-street/studio-sdk-python/commit/7d853cbb2a3451bea88c923e9a6aa0725340f51c))
* go live ([#2](https://github.com/clear-street/studio-sdk-python/issues/2)) ([b8be4a5](https://github.com/clear-street/studio-sdk-python/commit/b8be4a51ff1a7ba9775448430f4e77b11aaaaa6c))
* update SDK settings ([c6b7eeb](https://github.com/clear-street/studio-sdk-python/commit/c6b7eeb315a6111b886363b1983dacfab2e915bc))
