## News portal

---

### Setup:

---

```
git clone git@github.com:Kvazitropter/news-portal.git
cd news-portal
make install
```
```
# generate SECRET_KEY:
make console
>>> ```from django.core.management.utils import get_random_secret_key```
>>> ```print(get_random_secret_key())```
# insert SECRET_KEY and other parameters to /.env
```
```
make dev
```

---