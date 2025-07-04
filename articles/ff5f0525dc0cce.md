---
title: "Pythonの__repr__と__str__と__format__の違いを理解する"
emoji: "🐥"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: [python, python3]
published: false
---

# 目的

Pythonの組み込み関数である**repr**、**str**、**format**の役割がわかる

# 環境情報

- Python：3.13.5

# object.**repr**の役割

組み込み関数のrepr()から呼び出される。 objectの公式な文字列表現を返す。
同じ値を使ってオブジェクトを再生成することができるようなPython表現式となっていることが理想的。
実現が難しければ`<...some useful description...>`のような文字列を返すべき
また**repr**が定義されているが、**str**が存在しない場合、**repr**は非公式の文字列表現としても使用される。
典型的な使用例としてはデバッグログへの表示が挙げられる。情報量が豊富で曖昧性が排除された表現が理想的。デフォルトの実装はobject classによって提供される。

# **str**の役割

# **format**の役割
