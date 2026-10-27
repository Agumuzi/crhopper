<div align="center">

<img src="docs/assets/rocket.svg" alt="CR-Hopper pixel rocket" width="105" height="105">

# CR-Hopper

**面向 Hiddify、Mihomo 与 Clash 兼容客户端的精选公共代理订阅。**

[English](./README.md) · [简体中文](./README.zh-CN.md) · [Русский](./README.ru.md) · [فارسی](./README.fa.md)

[**项目官网 / 一键复制订阅**](https://agumuzi.github.io/crhopper/) · [☕ 支持开发](https://ko-fi.com/agumuzi)

</div>

---

## 订阅链接

### Hiddify / URI 订阅

复制下面的链接，在 Hiddify 或其他支持 URI 订阅的客户端中添加为远程配置。

```text
https://raw.githubusercontent.com/Agumuzi/crhopper/main/CR-Hopper.txt
```

### Mihomo / Clash YAML

复制下面的链接，在 Mihomo / Clash 兼容客户端中作为远程 YAML 配置使用。

```text
https://raw.githubusercontent.com/Agumuzi/crhopper/main/CR-Hopper.yaml
```

## CR-Hopper 是什么？

CR-Hopper 发布一组在公开前已经完成上游筛选与运行时准备的代理节点。

CR-Hopper 处理的上游代理候选均来自互联网上已经公开可获取的来源。本项目不创建、不托管、也不运营这些上游节点；CR-Hopper 只负责对公开节点进行收集、筛选、验证，并将通过筛选的子集整理为客户端可直接使用的订阅格式后重新发布。

公开订阅可能包含 VLESS、Hysteria2、Shadowsocks 等多种协议。每次更新后的节点数量和协议构成都可能变化。

## 推荐客户端

- **Hiddify：** 使用 `CR-Hopper.txt`
- **Mihomo / Clash 兼容客户端：** 使用 `CR-Hopper.yaml`

## 使用说明

- 公共节点可能随时失效；连接异常时请先刷新订阅。
- 客户端显示的 Geo 地理位置由客户端自行判断，可能与节点名称中的标签不同。
- TXT 与 YAML 是同一批公开节点的不同订阅格式。

## Google Drive 内部同步说明

**CR-Hopper Sync** 是仅由项目维护者使用的 Google Drive 归档组件。独立运行的本地筛选系统通过 `rclone` 将项目文件与运行证据同步到维护者自己的云盘。**这不是公开订阅用户的 Google 登录功能**：使用 TXT/YAML 订阅无需 Google 授权，原订阅链接不变。私人扫描文件及 OAuth 凭据不会放入公开仓库。

[查看 CR-Hopper Sync 隐私政策](https://agumuzi.github.io/crhopper/privacy.html)，了解数据访问、保存、删除和撤销授权方式。

## 免责声明

CR-Hopper 仅提供用于测试、研究及个人网络用途的公共订阅数据。

使用者有责任自行确认其对本仓库、订阅链接以及其中第三方代理节点的使用行为，符合其所在国家或地区适用的法律法规、合同义务以及相关服务条款。**不得在违反当地法律法规的情况下使用 CR-Hopper，也不得将本项目用于任何当地法律法规明确禁止的用途。**

本项目的开发者与维护者不运营、不控制，也不保证公开订阅中第三方代理节点的实际状态。节点的可用性、速度、安全性、隐私性、稳定性、实际出口地区及持续运行能力均不作任何保证。

本项目按 **“现状”** 和 **“可用状态”** 提供，不提供任何明示或默示担保。使用者应自行承担使用本项目产生的全部风险，并自行对其网络行为、数据、账号、设备以及合规义务负责。

在适用法律允许的最大范围内，本项目开发者与维护者不对使用者滥用本项目、实施违法行为、服务中断、账号受限、数据丢失或泄露、安全事件、经济损失、法律后果，以及因使用或无法使用 CR-Hopper 所产生的任何直接或间接损失承担责任。
