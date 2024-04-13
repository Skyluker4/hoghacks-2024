// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'situation.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Situation _$SituationFromJson(Map<String, dynamic> json) => Situation(
      away_score: json['away_score'] as int,
      home_score: json['home_score'] as int,
      is_possessing_team: json['is_possessing_team'] as bool,
      position: Position.fromJson(json['position'] as Map<String, dynamic>),
      quarter: json['quarter'] as int,
      time: json['time'] as String,
    );

Map<String, dynamic> _$SituationToJson(Situation instance) => <String, dynamic>{
      'away_score': instance.away_score,
      'home_score': instance.home_score,
      'is_possessing_team': instance.is_possessing_team,
      'position': instance.position,
      'quarter': instance.quarter,
      'time': instance.time,
    };

Position _$PositionFromJson(Map<String, dynamic> json) => Position(
      distance: json['distance'] as int,
      down: json['down'] as int,
      yard: json['yard'] as int,
    );

Map<String, dynamic> _$PositionToJson(Position instance) => <String, dynamic>{
      'distance': instance.distance,
      'down': instance.down,
      'yard': instance.yard,
    };
