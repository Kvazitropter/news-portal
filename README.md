# News portal

---

## Setup:

---

#### Clone repository:
```bash
git clone git@github.com:Kvazitropter/news-portal.git
```

#### Install dependencies:
```bash
cd news-portal
make install
```

#### Generate SECRET_KEY:
```bash
make console
```
`In console:`
```bash
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```
`Insert generated key and other parameters in /.env`

#### Run server:
```
make dev
```

---
