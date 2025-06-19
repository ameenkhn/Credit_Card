import React, { useState } from 'react';
import {
  Box,
  TextField,
  Button,
  Typography,
  Grid,
  Alert,
} from '@mui/material';

interface SpendingFormProps {
  formData: any;
  setFormData: (data: any) => void;
  onNext: () => void;
  onBack: () => void;
}

const SpendingForm: React.FC<SpendingFormProps> = ({
  formData,
  setFormData,
  onNext,
  onBack,
}) => {
  const [errors, setErrors] = useState<{ [key: string]: string }>({});

  const validateForm = () => {
    const newErrors: { [key: string]: string } = {};
    const spendingHabits = formData.spending_habits || {};

    if (!spendingHabits.fuel || spendingHabits.fuel <= 0) {
      newErrors.fuel = 'Please enter a valid fuel expense';
    }
    if (!spendingHabits.travel || spendingHabits.travel <= 0) {
      newErrors.travel = 'Please enter a valid travel expense';
    }
    if (!spendingHabits.groceries || spendingHabits.groceries <= 0) {
      newErrors.groceries = 'Please enter a valid groceries expense';
    }
    if (!spendingHabits.dining || spendingHabits.dining <= 0) {
      newErrors.dining = 'Please enter a valid dining expense';
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (validateForm()) {
      onNext();
    }
  };

  const handleSpendingChange = (category: string, value: string) => {
    const numValue = parseFloat(value) || 0;
    setFormData({
      ...formData,
      spending_habits: {
        ...formData.spending_habits,
        [category]: numValue,
      },
    });
    // Clear error when user starts typing
    if (errors[category]) {
      setErrors({
        ...errors,
        [category]: '',
      });
    }
  };

  return (
    <Box component="form" onSubmit={handleSubmit} sx={{ mt: 2 }}>
      <Typography variant="h6" gutterBottom>
        Tell us about your monthly spending
      </Typography>

      {Object.keys(errors).length > 0 && (
        <Alert severity="error" sx={{ mb: 2 }}>
          Please fill in all spending categories with valid amounts
        </Alert>
      )}

      <Grid container spacing={2}>
        <Grid item xs={12} sm={6}>
          <TextField
            fullWidth
            label="Fuel Expenses (₹)"
            type="number"
            value={formData.spending_habits?.fuel || ''}
            onChange={(e) => handleSpendingChange('fuel', e.target.value)}
            margin="normal"
            required
            error={!!errors.fuel}
            helperText={errors.fuel}
            InputProps={{
              inputProps: { min: 0, step: "100" }
            }}
          />
        </Grid>
        <Grid item xs={12} sm={6}>
          <TextField
            fullWidth
            label="Travel Expenses (₹)"
            type="number"
            value={formData.spending_habits?.travel || ''}
            onChange={(e) => handleSpendingChange('travel', e.target.value)}
            margin="normal"
            required
            error={!!errors.travel}
            helperText={errors.travel}
            InputProps={{
              inputProps: { min: 0, step: "100" }
            }}
          />
        </Grid>
        <Grid item xs={12} sm={6}>
          <TextField
            fullWidth
            label="Groceries Expenses (₹)"
            type="number"
            value={formData.spending_habits?.groceries || ''}
            onChange={(e) => handleSpendingChange('groceries', e.target.value)}
            margin="normal"
            required
            error={!!errors.groceries}
            helperText={errors.groceries}
            InputProps={{
              inputProps: { min: 0, step: "100" }
            }}
          />
        </Grid>
        <Grid item xs={12} sm={6}>
          <TextField
            fullWidth
            label="Dining Expenses (₹)"
            type="number"
            value={formData.spending_habits?.dining || ''}
            onChange={(e) => handleSpendingChange('dining', e.target.value)}
            margin="normal"
            required
            error={!!errors.dining}
            helperText={errors.dining}
            InputProps={{
              inputProps: { min: 0, step: "100" }
            }}
          />
        </Grid>
      </Grid>

      <Box sx={{ mt: 3, display: 'flex', justifyContent: 'space-between' }}>
        <Button onClick={onBack}>Back</Button>
        <Button
          type="submit"
          variant="contained"
          color="primary"
        >
          Next
        </Button>
      </Box>
    </Box>
  );
};

export default SpendingForm; 