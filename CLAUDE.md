# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## プロジェクト概要

このリポジトリはZennの記事と本のコンテンツを管理するためのものです。Zenn CLIを使用して、記事や本の作成、プレビュー、管理を行います。

## ディレクトリ構造

- `articles/` - Zennの記事を格納するディレクトリ
- `books/` - Zennの本を格納するディレクトリ

## よく使うコマンド

### プレビュー
```bash
npx zenn preview
```
ローカルサーバーを起動してブラウザで記事や本をプレビューします。

### 新しい記事の作成
```bash
npx zenn new:article
```
新しい記事のマークダウンファイルを`articles/`ディレクトリに作成します。

### 新しい本の作成
```bash
npx zenn new:book
```
新しい本のディレクトリと設定ファイルを`books/`ディレクトリに作成します。

### 記事の一覧表示
```bash
npx zenn list:articles
```

### 本の一覧表示
```bash
npx zenn list:books
```

## コンテンツの管理

- 記事と本はすべてMarkdown形式で記述されます
- 各ファイルにはFront Matterでメタデータ(タイトル、公開ステータス、タグなど)を設定します
- 詳細なガイドは https://zenn.dev/zenn/articles/zenn-cli-guide を参照してください
