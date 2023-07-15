with import <nixpkgs> {};

mkShell {
  nativeBuildInputs = [
    python3
  ];
  buildInputs = with python310Packages; [
    pygame
  ];

}
