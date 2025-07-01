---
title: "Pythonの__repr__と__str__と__format__の役割の違いを理解する"
emoji: "🐥"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: []
published: false
---

# はじめに

# **repr**の役割

組み込み関数のrepr()から呼び出される
objectの公式な文字列表現を返す
同じ値を使ってオブジェクトを再生成することができるようなPython表現式となっていることが理想的
実現が難しければ`<...some useful description...>`のような文字列を返すべき
また**repr**が定義されているが、**str**が存在しない場合、**repr**は非公式の文字列表現としても使用される

# **str**の役割

# **format**の役割
