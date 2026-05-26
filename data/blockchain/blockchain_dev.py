"""区块链开发工程师数据"""
data = {
    '计算机与信息技术': {
        '区块链': {
            '区块链开发工程师': {
                'description': '开发区块链应用和智能合约，构建去中心化系统。',
                'skills': {
                    'Go': {
                        'desc': '区块链底层开发，如Fabric、以太坊客户端',
                        'difficulty': 1,
                        'dimensions': [
                            ['Go基础语法/数据类型', 'Goroutine协程/并发', 'Channel通道通信', 'defer/panic/recover', 'net/http网络编程', 'gRPC框架', 'database/sql', 'Redis客户端', 'Protocol Buffer', '日志/zap/logrus', '测试/testing', 'Docker容器化', '微服务架构', '密码学基础', '区块链sdk/go-ethereum']
                        ]
                    },
                    'Rust': {
                        'desc': '高性能区块链开发，如Solana、Polkadot',
                        'difficulty': 1,
                        'dimensions': [
                            ['Rust基础/所有权/借用', '数据类型/结构体/枚举', 'Trait特征/接口', 'Error处理', 'Option/Result', 'Iterator迭代器', '生命周期/Lifetime', '并发/Send/Sync', 'Async/Await异步', 'Crates包管理', 'Cargo构建', '宏/Macro', '所有权系统', '智能指针/Box', 'WASM编译']
                        ]
                    },
                    'Solidity': {
                        'desc': '以太坊智能合约开发语言',
                        'difficulty': 1,
                        'dimensions': [
                            ['Solidity语法/版本', '数据类型/int/address/string', '函数可见性/public/private', '函数修饰符/modifier', '事件/Event', '继承/接口', '库/Library', 'Fallback函数', 'Receive函数', 'Gas优化', '存储/内存/Memory', 'Try/Catch', 'ABI接口', 'Web3.py调用', '合约安全']
                        ]
                    },
                    'DApp开发': {
                        'desc': '去中心化应用前后端开发',
                        'difficulty': 2,
                        'dimensions': [
                            ['DApp架构/前端+合约', 'Web3.js连接钱包', 'ethers.js库', 'MetaMask钱包集成', '合约交互/Call/Send', '签名交易', '前端框架/React/Vue', 'IPFS去中心化存储', 'ENS域名解析', 'Chainlink预言机', '去中心化身份/DID', 'DApp部署/IPFS', 'Gas费用计算', '测试网/Faucet', '主网部署']
                        ]
                    },
                    'NFT': {
                        'desc': '非同质化代币标准和应用',
                        'difficulty': 2,
                        'dimensions': [
                            ['NFT标准/ERC721/ERC1155', 'TokenURI元数据', 'IPFS存储/NFT metadata', '铸造/Mint NFT', '转移/Transfer', '所有权/Owner', '批量铸造/Batch', 'NFT市场/OpenSea', 'NFT合约开发', 'ERC721A优化', 'NFT安全性检查', '版税机制/Royalty', '链上元数据/On-chain', '动态NFT', 'NFT游戏化']
                        ]
                    },
                    'Web3.js': {
                        'desc': '与区块链交互的JavaScript库',
                        'difficulty': 2,
                        'dimensions': [
                            ['Web3.js安装配置', 'Provider连接/HttpProvider', 'Web3实例创建', '账户/Accounts', '合约实例/Contract', '交易/SendTransaction', '事件监听/Events', '签名/Sign', 'Call调用/read', 'Gas估算', '区块查询/Block', '日志查询/Filter', 'ABI接口', '合约部署/Deploy', '测试网连接']
                        ]
                    },
                    '以太坊': {
                        'desc': 'EVM原理、Gas机制、交易流程',
                        'difficulty': 2,
                        'dimensions': [
                            ['以太坊概述/ETH', 'EVM虚拟机原理', '账户/EOA/Contract', '交易结构/nonce/gas/value', 'Gas费用/GasPrice/GasLimit', '区块结构/Header', 'Merkle Tree/Patricia Trie', 'Solidity语言', 'EVM执行/Opcode', '预编译合约', '叔块/Uncle', '难度调整/Difficulty', 'Ethash工作量证明', '账户抽象/AA', '分片/Sharding']
                        ]
                    },
                    '链上数据分析': {
                        'desc': '区块链浏览器、事件监听',
                        'difficulty': 2,
                        'dimensions': [
                            ['Etherscan浏览器', '区块查询/Block Number', '交易查询/TxHash', '合约事件/Events', '日志解析/Log', 'ABI解码', '链上数据/The Graph', 'GraphQL查询', '链分析/Dune Analytics', 'Grafana链上监控', 'Nansen工具', '合约调用追踪', 'Flashbots/MEV', '代币转账追踪', '鲸鱼地址追踪']
                        ]
                    },
                    'DeFi': {
                        'desc': '去中心化金融协议开发',
                        'difficulty': 3,
                        'dimensions': [
                            ['DeFi概述/AMM/借贷', 'Uniswap兑换协议', 'DEX流动性', 'AMM公式/x*y=k', '流动性挖矿/Liquidity Mining', 'Compound借贷', 'Aave闪电贷', 'Yield Farming', '代币Swap', '流动性池/LP', '无常损失/IL', '预言机喂价/Chainlink', 'DeFi聚合器/Yearn', '治理代币/Governance', 'DeFi安全审计']
                        ]
                    },
                    '共识算法': {
                        'desc': 'PoW、PoS、DPoS等共识机制',
                        'difficulty': 3,
                        'dimensions': [
                            ['共识算法概述', 'PoW工作量证明', 'SHA256哈希', '挖矿/Mining', '区块奖励/Block Reward', '难度调整/Difficulty Target', 'PoS权益证明', '验证者/Validator', '质押/Staking', 'BFT拜占庭容错', 'PBFT实用拜占庭', 'DPoS委托权益', 'Tendermint', 'HotStuff', 'Casper FFG']
                        ]
                    },
                    '密码学': {
                        'desc': '哈希、签名、零知识证明',
                        'difficulty': 3,
                        'dimensions': [
                            ['哈希函数/SHA256/Keccak', 'Merkle Tree', '椭圆曲线/ECC/secp256k1', 'ECDSA签名', '公钥/私钥', '数字签名', '零知识证明/ZK-SNARKs', 'ZK-STARKs', 'Merkle Proof', 'Pedersen承诺', 'Poseidon哈希', '环签名/Ring Signature', '多签/Multisig', '门限签名/TSS', '同态加密']
                        ]
                    },
                    '智能合约': {
                        'desc': '编写、测试、部署智能合约',
                        'difficulty': 3,
                        'dimensions': [
                            ['智能合约概述', 'Solidity开发环境/Truffle/Hardhat', '合约编写/ERC20/ERC721', '测试框架/Waffle/Mocha', '部署脚本', 'Truffle Migrations', 'Hardhat配置', 'OpenZeppelin库', '合约安全漏洞/Reentrancy', '安全审计/Slither', '形式化验证', 'Gas优化技巧', '代理合约/EIP1167', '升级合约/UUPS/Transparent', '多链部署']
                        ]
                    }
                }
            }
        }
    }
}