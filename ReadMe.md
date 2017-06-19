# このソフトウェアについて

`./web/service/github/api/v3/Response.py`の単体テストをした。実質結合テスト。

ContentType関係のクラス一式を`./web/http/`配下に結合してテストした。

* `Response.py`の変更
    * ContentType関係の変更を反映した
    * ContentType文字列がNoneになるとMimeTypeクラスで例外発生するのでそのif文を削除した

# 前回までのGitHubアップローダ単体テスト用リポジトリ

対象ソースコード|単体テスト記事|単体テストGitHub
---------------|-------------|---------------
`./web/service/github/api/v3/authentication`|[http://ytyaru.hatenablog.com/entry/2017/11/29/000000:title]|[GitHub.API.Authentication.Abstract.201704141006](https://github.com/ytyaru/GitHub.API.Authentication.Abstract.201704141006)
`.cui/register/SshConfigurator.py`|[http://ytyaru.hatenablog.com/entry/2017/12/10/000000:title]|[Github.Uploader.SshConfigurator.unittest.201704221606](https://github.com/ytyaru/Github.Uploader.SshConfigurator.unittest.201704221606)
`.cui/register/SshKeyGen.py`|[http://ytyaru.hatenablog.com/entry/2017/12/11/000000:title]|[Github.Uploader.SshKeyGen.unittest.201704221809](https://github.com/ytyaru/Github.Uploader.SshKeyGen.unittest.201704221809)|[Github.Uploader.SshKeyGen.unittest.201704221809](https://github.com/ytyaru/Github.Uploader.SshKeyGen.unittest.201704221809)
`./web/sqlite/Json2Sqlite.py|[http://ytyaru.hatenablog.com/entry/2017/12/13/000000:title]|[Github.Uploader.Json2Sqlite.unittest.201704230804](https://github.com/ytyaru/Github.Uploader.Json2Sqlite.unittest.201704230804)
`./web/log/Log.py`|[http://ytyaru.hatenablog.com/entry/2017/12/20/000000:title]|[GitHub.Uploader.Log.unittest.201704251509](https://github.com/ytyaru/GitHub.Uploader.Log.unittest.201704251509)
`./web/http/Response.py`|[http://ytyaru.hatenablog.com/entry/2017/12/29/000000:title]|[GitHub.Uploader.ContentType.201705040739](https://github.com/ytyaru/GitHub.Uploader.ContentType.201705040739)
`./web/service/github/api/v3/AuthenticationsCreator.py`|[http://ytyaru.hatenablog.com/entry/2017/12/31/000000:title]|[Github.Uploader.AuthenticationsCreator.unittest.201705041033](https://github.com/ytyaru/Github.Uploader.AuthenticationsCreator.unittest.201705041033)
`./web/service/github/api/v3/RequestParameter.py`|[http://ytyaru.hatenablog.com/entry/2017/01/02/000000:title]|[Github.Uploader.RequestParameter.unittest.201705041425](https://github.com/ytyaru/Github.Uploader.RequestParameter.unittest.201705041425)

# 開発環境

* Linux Mint 17.3 MATE 32bit
* [Python 3.4.3](https://www.python.org/downloads/release/python-343/)
* [SQLite](https://www.sqlite.org/) 3.8.2

## WebService

* [GitHub](https://github.com/)
    * [アカウント](https://github.com/join?source=header-home)
    * [AccessToken](https://github.com/settings/tokens)
    * [Two-Factor認証](https://github.com/settings/two_factor_authentication/intro)
    * [API v3](https://developer.github.com/v3/)

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

Library|License|Copyright
-------|-------|---------
[requests](http://requests-docs-ja.readthedocs.io/en/latest/)|[Apache-2.0](https://opensource.org/licenses/Apache-2.0)|[Copyright 2012 Kenneth Reitz](http://requests-docs-ja.readthedocs.io/en/latest/user/intro/#requests)
[dataset](https://dataset.readthedocs.io/en/latest/)|[MIT](https://opensource.org/licenses/MIT)|[Copyright (c) 2013, Open Knowledge Foundation, Friedrich Lindenberg, Gregor Aisch](https://github.com/pudo/dataset/blob/master/LICENSE.txt)
[bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)|[MIT](https://opensource.org/licenses/MIT)|[Copyright © 1996-2011 Leonard Richardson](https://pypi.python.org/pypi/beautifulsoup4),[参考](http://tdoc.info/beautifulsoup/)
[pytz](https://github.com/newvem/pytz)|[MIT](https://opensource.org/licenses/MIT)|[Copyright (c) 2003-2005 Stuart Bishop <stuart@stuartbishop.net>](https://github.com/newvem/pytz/blob/master/LICENSE.txt)
[furl](https://github.com/gruns/furl)|[Unlicense](http://unlicense.org/)|[gruns/furl](https://github.com/gruns/furl/blob/master/LICENSE.md)
[PyYAML](https://github.com/yaml/pyyaml)|[MIT](https://opensource.org/licenses/MIT)|[Copyright (c) 2006 Kirill Simonov](https://github.com/yaml/pyyaml/blob/master/LICENSE)

