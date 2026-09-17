"""Which pattern lands in which slot.

The machine's four pattern pages are a navigation surface, not a filing
cabinet: while playing you reach for a page, not a pattern number. So the
banks are arranged by *feel of the kick* rather than by genre.

  pages 1-2  kick-forward - four-to-the-floor, tresillo, driving syncopation
  pages 3-4  everything else - breaks, song styles, percussion, texture

Within pages 1 and 2 the split is straight-four first, displaced kicks second,
so page 1 is the steadiest material on the machine and page 2 is where the
groove starts pulling against the grid.
"""

TT606_ORDER = [
    # page 1 (red) - four-to-the-floor
    "House", "Deep House", "Tech House", "Techno",
    "Hard Techno", "Minimal", "Dub Techno", "Detroit Techno",
    "Acid Techno", "Hardgroove", "Schranz", "Trance",
    "Hardcore", "EBM", "Motorik", "Disco",
    # page 2 (yellow) - tresillo and kick-driven syncopation
    "Tresillo", "Tresillo Techno", "Half Tresillo", "Dembow",
    "Baile Funk", "Samba Electro", "Miami Bass", "Baltimore Club",
    "Footwork", "Electro", "Big Beat", "Broken Beat",
    "Industrial Techno", "Ghetto House", "Afro House", "Nu-Disco",
    # page 3 (green) - breaks, rock and wave
    "Breakbeat", "Boom Bap", "Trip-Hop", "Jungle",
    "Drum & Bass", "Halftime", "Funk Break", "Amen Feel",
    "UK Garage", "606 Rock", "Post-Punk", "Coldwave",
    "Synth-Pop", "Italo", "Freestyle", "New Beat",
    # page 4 (blue) - grooves, texture and polyrhythm
    "Psy", "Tribal Techno", "IDM Glitch", "Braindance",
    "Cut-Up", "Shoegaze Drive", "Noise Industrial", "16th Shuffle",
    "Swung Boom Bap", "Reggaeton", "6/8 Feel", "Cumbia Machine",
    "Bossa Electro", "Boogie", "Polyrhythm 5", "Drone Pulse",
]

TT78_ORDER = [
    # page 1 (red) - four-to-the-floor and straight drive
    "Disco 1", "Disco 2", "House 78", "Deep House 78",
    "Nu-Disco 78", "Italo 78", "Cosmic Disco", "Motorik 78",
    "Krautrock Shuffle", "Steppers", "Minimal 78", "Balearic",
    "Foxtrot", "Tambourine Pulse", "Cowbell Drive", "Guiro Groove",
    # page 2 (yellow) - tresillo and kick-driven latin
    "Tresillo", "Tresillo Cumbia", "Half Tresillo", "Dembow 78",
    "Baile 78", "Samba", "Soukous", "Merengue",
    "Cumbia", "Bomba", "Highlife", "Afro House 78",
    "Broken 78", "Cha-Cha", "Mambo", "Songo",
    # page 3 (green) - CR-78 heritage and song styles
    "Rock 1", "Rock 2", "Slow Rock", "Swing",
    "Shuffle", "Waltz Feel", "Bossa Nova", "Rhumba",
    "Tango", "Beguine", "Synth-Pop 78", "City Pop",
    "Boogie 78", "Lo-Fi", "Downtempo", "Trip-Hop 78",
    # page 4 (blue) - latin percussion, dub and polyrhythm
    "Guaguanco", "Plena", "Salsa", "Afrobeat",
    "Bembe 6/8", "Calypso", "One Drop", "Dub",
    "Nyabinghi", "Conga Workout", "Bongo Cascara", "Clave & Maracas",
    "Reggaeton 78", "Poly 3:4", "Poly 5", "Free Percussion",
]

PAGE_TITLES = {
    "TT-606": ["Four-to-the-floor", "Tresillo & kick-driven",
               "Breaks, rock & wave", "Grooves, texture & polyrhythm"],
    "TT-78": ["Four-to-the-floor & drive", "Tresillo & kick-driven latin",
              "CR-78 heritage & song styles", "Latin percussion, dub & polyrhythm"],
}


def reorder(styles, order, machine):
    """Return `styles` arranged into `order`, checking the two agree exactly."""
    by_name = {s.name: s for s in styles}
    missing = [n for n in order if n not in by_name]
    extra = [n for n in by_name if n not in order]
    if missing or extra:
        raise ValueError(
            f"{machine}: order lists {len(order)} names; "
            f"missing from styles {missing}; not placed in any page {extra}")
    if len(order) != 64:
        raise ValueError(f"{machine}: order has {len(order)} entries, expected 64")
    return [by_name[n] for n in order]
