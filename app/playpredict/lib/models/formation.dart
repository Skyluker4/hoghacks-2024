// ignore_for_file: non_constant_identifier_names

import 'package:json_annotation/json_annotation.dart';

part 'formation.g.dart';

@JsonSerializable()
class Formation {
  Formation({
    required this.image,
    required this.name,
    required this.weight,
  });

  factory Formation.fromJson(Map<String, dynamic> json) =>
      _$FormationFromJson(json);

  final String image;
  final String name;
  final double weight;

  Map<String, dynamic> toJson() => _$FormationToJson(this);
}
