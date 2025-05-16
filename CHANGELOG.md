# [3.1.0](https://github.com/Basis-Theory/python-connections-sdk/compare/v3.0.0...v3.1.0) (2025-05-16)


### Features

* moving to suggested property for NTTxId ([#43](https://github.com/Basis-Theory/python-connections-sdk/issues/43)) ([e69ba68](https://github.com/Basis-Theory/python-connections-sdk/commit/e69ba68cd98b150672134fbad0008b8bccf654b0))

# [3.0.0](https://github.com/Basis-Theory/python-connections-sdk/compare/v2.1.0...v3.0.0) (2025-05-15)


### Features

* adding additional CKO error code mappings, Error Response Updates, and BT Trace Id ([#42](https://github.com/Basis-Theory/python-connections-sdk/issues/42)) ([1dbd579](https://github.com/Basis-Theory/python-connections-sdk/commit/1dbd579b97ddd821bf6631d249ccef1676884e3f))


### BREAKING CHANGES

* Returning processing errors in TransactionResponse

# [2.1.0](https://github.com/Basis-Theory/python-connections-sdk/compare/v2.0.0...v2.1.0) (2025-05-13)


### Features

* 3DS enhancements ([#41](https://github.com/Basis-Theory/python-connections-sdk/issues/41)) ([784abd5](https://github.com/Basis-Theory/python-connections-sdk/commit/784abd5fa6d3cc8028cbb52d1491ba2af4d146b4))

# [2.0.0](https://github.com/Basis-Theory/python-connections-sdk/compare/v1.1.0...v2.0.0) (2025-04-18)


### Bug Fixes

* fixing build pipeline versions ([#40](https://github.com/Basis-Theory/python-connections-sdk/issues/40)) ([fea59c5](https://github.com/Basis-Theory/python-connections-sdk/commit/fea59c579fee900854c3d7653a9fe7a65ab181a0))


### Features

* removing singleton to avoid shared state ([#39](https://github.com/Basis-Theory/python-connections-sdk/issues/39)) ([50023b0](https://github.com/Basis-Theory/python-connections-sdk/commit/50023b0a5c4806f612271bb3a82cd3a13aee19b3))


### BREAKING CHANGES

* Moving from `Connections.init(...)` to `Connections(...)` to load SDK config

# [1.1.0](https://github.com/Basis-Theory/python-connections-sdk/compare/v1.0.0...v1.1.0) (2025-04-15)


### Features

* fixing gap to allow 0 amounts ([#38](https://github.com/Basis-Theory/python-connections-sdk/issues/38)) ([d10b087](https://github.com/Basis-Theory/python-connections-sdk/commit/d10b087b7fc4fcc640ef12eb1543a10f180258c5))

# [1.0.0](https://github.com/Basis-Theory/python-connections-sdk/compare/v0.1.0...v1.0.0) (2025-03-12)


### Features

* moving to sync methods vs async ([#36](https://github.com/Basis-Theory/python-connections-sdk/issues/36)) ([845da24](https://github.com/Basis-Theory/python-connections-sdk/commit/845da24b594adccc978fa228d3c5bd6e66e9a034))


### BREAKING CHANGES

* will no longer need to await or asyncio

# [0.1.0](https://github.com/Basis-Theory/python-connections-sdk/compare/v0.0.1...v0.1.0) (2025-02-12)


### Bug Fixes

* adding checkout with to the release workflow ([#31](https://github.com/Basis-Theory/python-connections-sdk/issues/31)) ([e67b853](https://github.com/Basis-Theory/python-connections-sdk/commit/e67b853356be87fcf285b7a1d3afb26d9df3b538))
* adding semantic config ([#27](https://github.com/Basis-Theory/python-connections-sdk/issues/27)) ([bd39aa9](https://github.com/Basis-Theory/python-connections-sdk/commit/bd39aa991336e23ff644a60a98a421d88454a587))
* checking out as semantic user ([#30](https://github.com/Basis-Theory/python-connections-sdk/issues/30)) ([1346734](https://github.com/Basis-Theory/python-connections-sdk/commit/13467342ac859320fd8c63d64e50b5874a396f97))
* input name for semantic ([#33](https://github.com/Basis-Theory/python-connections-sdk/issues/33)) ([f18f627](https://github.com/Basis-Theory/python-connections-sdk/commit/f18f6279956c6087df48f2e12b92cfc17970c3e0))
* lowering the python version to earlier version ([#19](https://github.com/Basis-Theory/python-connections-sdk/issues/19)) ([9608312](https://github.com/Basis-Theory/python-connections-sdk/commit/96083129d64c07681d84dddbe656d69d85f51a50))
* repo name for semantic release ([#26](https://github.com/Basis-Theory/python-connections-sdk/issues/26)) ([9cdc92f](https://github.com/Basis-Theory/python-connections-sdk/commit/9cdc92fc37f6728b583eda9ca01e1e62548b150d))
* wrong secret name ([#28](https://github.com/Basis-Theory/python-connections-sdk/issues/28)) ([8f6b4e7](https://github.com/Basis-Theory/python-connections-sdk/commit/8f6b4e7a376b57cc7acad80355879421ffd56bc0))


### Features

* adding metadata mappings ([#20](https://github.com/Basis-Theory/python-connections-sdk/issues/20)) ([99267f4](https://github.com/Basis-Theory/python-connections-sdk/commit/99267f44c82425b71ca89f15b376c2f2aa6476ff))
* adding pervious transaction id mappings ([#21](https://github.com/Basis-Theory/python-connections-sdk/issues/21)) ([996241c](https://github.com/Basis-Theory/python-connections-sdk/commit/996241c637abe196773e6ac5f75d91aee1b8932d))
* adding provider overrides for additional data and snake_case ([#22](https://github.com/Basis-Theory/python-connections-sdk/issues/22)) ([afbd9a3](https://github.com/Basis-Theory/python-connections-sdk/commit/afbd9a399f799d9e43cc48d8ebc4afbae50d901a))
* adding refund and refactoring to use models ([#18](https://github.com/Basis-Theory/python-connections-sdk/issues/18)) ([fd66ec2](https://github.com/Basis-Theory/python-connections-sdk/commit/fd66ec29d56df479ef1c8f73b1866f31ec4cb362))
