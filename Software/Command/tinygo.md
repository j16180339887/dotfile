Install for docker archlinux
=====
```sh
app-fast -S go clang llvm lld --needed
go get -d github.com/tinygo-org/tinygo
cd $GOPATH/src/github.com/tinygo-org/tinygo
GO111MODULE=on go mod vendor
go install
```

Webassembly
=====
* Compile main.go to main.wasm
* $ tinygo build -o main.wasm -target wasm -no-debug ./main.go

