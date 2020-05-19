{
    "targets": [
        {
            "target_name": "cuckaroo29b-hashing",
            "sources": [
                "cuckaroo29b.cc",
                "src/blake2b-ref.c"
            ],
            "include_dirs": [
                "src",
                "<!(node -e \"require('nan')\")"
            ]
        }
    ]
}
