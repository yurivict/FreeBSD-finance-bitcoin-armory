# Created by: Yuri Victorovich <yuri@rawbw.com>
# $FreeBSD: head/finance/bitcoin-armory/Makefile 433310 2017-02-04 13:37:15Z tcberner $

PORTNAME=	BitcoinArmory
PORTVERSION=	0.96
DISTVERSIONPREFIX=	v
DISTVERSIONSUFFIX=	-testing
CATEGORIES=	finance

MAINTAINER=	yuri@rawbw.com
COMMENT=	Desktop bitcoin management system

LICENSE=	AGPLv3
LICENSE_FILE=	${WRKSRC}/LICENSE

BUILD_DEPENDS=	${LOCALBASE}/bin/swig3.0:devel/swig30 \
		${LOCALBASE}/bin/pyrcc4:textproc/py-qt4-xml \
		${LOCALBASE}/bin/rsync:net/rsync
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}qt4-core>=${PYQT4_VERSION}:devel/py-qt4-core \
		${PYTHON_PKGNAMEPREFIX}qt4-network>=${PYQT4_VERSION}:${PORTSDIR}/net/py-qt4-network \
		${PYTHON_PKGNAMEPREFIX}qt4-gui>=${PYQT4_VERSION}:x11-toolkits/py-qt4-gui \
		${PYTHON_PKGNAMEPREFIX}twistedCore>=14.0.0:devel/py-twistedCore \
		${PYTHON_PKGNAMEPREFIX}psutil>1.2.1:sysutils/py-psutil \
		${LOCALBASE}/bin/bitcoind:net-p2p/bitcoin-daemon

USE_GITHUB=	yes
GH_ACCOUNT=	goatpig
GH_TAGNAME=	dc50e4b
GH_TUPLE=	goatpig:libfcgi:b00dc69:x/cppForSwig/fcgi

USES=		autoreconf compiler:c++11-lang compiler:c++11-lib gmake pyqt:4 python:2 shebangfix
USE_PYQT=	core_run gui_run
GNU_CONFIGURE=	yes
SHEBANG_FILES=	dpkgfiles/armory extras/extractKeysFromWallet.py
CPPFLAGS+=	-I${LOCALBASE}/include
LDFLAGS+=	-L${LOCALBASE}/lib
CXXFLAGS+=	-DCRYPTOPP_DISABLE_ASM -fPIC
MAKE_ENV+=	PYTHON_CONFIG=${PYTHON_CMD}-config

#USE_GCC=	yes

MAKE_ARGS+=	CXXFLAGS="${CXXFLAGS}"
INSTALLS_ICONS=	yes
ICON_SIZES=	24x24 32x32 64x64

# When CRYPTOPP_DISABLE_ASM isn't needed any more, i386 amd64 should
# be made work through ASM code, and the other archs will still
# have CRYPTOPP_DISABLE_ASM

post-patch:
	@${REINPLACE_CMD} -i '' 's/python-config/$${PYTHON_CONFIG}/' ${WRKSRC}/configure.ac
	@${REINPLACE_CMD} -i '' 's/O_DSYNC/O_SYNC/' ${WRKSRC}/cppForSwig/lmdb/mdb.c
	@${REINPLACE_CMD} -i '' 's/std::tr1::/std::/g' ${WRKSRC}/cppForSwig/gtest/gtest.h

post-stage:
	@${REINPLACE_CMD} -i '' -e 's|%%LOCALBASE%%|${LOCALBASE}|g' ${STAGEDIR}/${LOCALBASE}/bin/armory
	@${REINPLACE_CMD} -i '' 's|Exec=/usr/bin/armory|Exec=${LOCALBASE}/bin/armory|' ${STAGEDIR}/${LOCALBASE}/share/applications/*.desktop
.for s in ${ICON_SIZES}
	@${MKDIR} ${STAGEDIR}${PREFIX}/share/icons/hicolor/${s}/apps/
	${MV} ${STAGEDIR}/${PREFIX}/share/armory/img/armory_icon_${s}.png \
		${STAGEDIR}${PREFIX}/share/icons/hicolor/${s}/apps/armoryicon.png
.endfor

post-install:
	@${RM} -f `${FIND} ${STAGEDIR}${PREFIX} -name "*.orig"`
	@${STRIP_CMD} ${STAGEDIR}${PREFIX}/lib/armory/_CppBlockUtils.so
	@${REINPLACE_CMD} -e 's|/usr/bin/ArmoryDB|${PREFIX}/bin/ArmoryDB|' ${STAGEDIR}${PREFIX}/lib/armory/SDM.py

do-test:
	@cd ${WRKSRC} && ${SETENV} ${MAKE_ENV} ${MAKE_CMD} test

.include <bsd.port.mk>
